from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
import requests
from django.conf import settings
from herosection.models import HeroSection
from .models import Packages, BookingPackage, Itinerary
from django.db.models import Q
from datetime import datetime
from decimal import Decimal


def package_list(request):
    """Display all tour packages with filtering options + weather forecast"""
    packages = Packages.objects.all()
    hero = HeroSection.objects.first()

    # Filtering
    category = request.GET.get('category')
    price = request.GET.get('price')
    destination = request.GET.get('destination')

    if category:
        packages = packages.filter(category=category)
    if destination:
        packages = packages.filter(destination__icontains=destination)
    if price:
        try:
            packages = packages.filter(price__lte=int(price))
        except (ValueError, TypeError):
            pass

    # Weather Forecast Section
    weather = None
    if destination:
        api_key = settings.OPENWEATHER_API_KEY
        try:
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={destination}&appid={api_key}&units=metric"
            )
            if response.status_code == 200:
                data = response.json()
                weather = {
                    'city': data['name'],
                    'temp': data['main']['temp'],
                    'desc': data['weather'][0]['description'].title(),
                    'icon': data['weather'][0]['icon'],
                    'humidity': data['main']['humidity'],
                    'wind': data['wind']['speed'],
                    'feels_like': data['main']['feels_like'],
                }
        except Exception as e:
            print("Weather API Error:", e)

    context = {
        'packages': packages,
        'hero': hero,
        'weather': weather,
        'categories': [
            ('honeymoon', 'Honeymoon'),
            ('family', 'Family'),
            ('adventure', 'Adventure'),
            ('weekend', 'Weekend Getaway'),
            ('luxury', 'Luxury'),
            ('budget', 'Budget'),
        ],
    }
    return render(request, 'package_list.html', context)


def package_detail(request, package_id):
    """Display detailed information about a specific package"""
    package = get_object_or_404(Packages, id=package_id)
    hero = HeroSection.objects.first()
    itineraries = Itinerary.objects.filter(package=package).order_by('day')
    similar_packages = Packages.objects.filter(
        destination=package.destination
    ).exclude(id=package_id)[:3]

    context = {
        'package': package,
        'itineraries': itineraries,
        'similar_packages': similar_packages,
        'hero':hero
    }
    return render(request, 'package_detail.html', context)


def booking(request, package_id):
    """Handle booking form for a package"""
    package = get_object_or_404(Packages, id=package_id)
    hero = HeroSection.objects.first()

    if request.method == 'POST':
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        travelers = int(request.POST.get('travelers', 1))
        start_date = request.POST.get('start_date')
        room_type = request.POST.get('room_type')
        special_requests = request.POST.get('special_requests', '')

        
        if not all([first_name, last_name, email, phone, address, start_date]):
            messages.error(request, 'Please fill all required fields.')
            return render(request, 'booking_package.html', {'package': package})

        try:
            
            subtotal = package.price * Decimal(travelers)
            gst = (subtotal * Decimal('0.18')).quantize(Decimal('0.01'))
            total_amount = (subtotal + gst).quantize(Decimal('0.01'))

            
            booking_obj = BookingPackage.objects.create(
                package=package,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                address=address,
                number_of_travelers=travelers,
                start_date=start_date,
                room_type=room_type,
                special_requests=special_requests,
                subtotal=subtotal,
                gst=gst,
                total_amount=total_amount,
                status='pending',
            )

            
            messages.success(
                request,
                f'Booking created successfully! Booking ID: {booking_obj.id}.'
            )

            
            return redirect('booking_confirmation', booking_id=booking_obj.id)

        except Exception as e:
            messages.error(request, f'Error creating booking: {str(e)}')
            return render(request, 'booking_package.html', {'package': package})

    context = {
        'package': package,
        'hero':hero 
    }
    return render(request, 'booking_package.html', context)


def booking_confirmation(request, booking_id):
    """Display booking confirmation page"""
    booking = get_object_or_404(BookingPackage, id=booking_id)
    hero = HeroSection.objects.first()
    context = {
        'booking': booking,
        'package': booking.package,
        'hero':hero
    }
    return render(request, 'booking_confirmation.html', context)


def search_packages(request):
    """Search packages with advanced filtering + live weather info"""
    query = request.GET.get('q', '')
    category = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    duration = request.GET.get('duration')

    hero = HeroSection.objects.first()

    packages = Packages.objects.all()

    # 🔍 Search logic
    if query:
        packages = packages.filter(
            Q(title__icontains=query) |
            Q(destination__icontains=query) |
            Q(description__icontains=query)
        )

    if category:
        packages = packages.filter(category=category)

    if min_price:
        try:
            packages = packages.filter(price__gte=int(min_price))
        except (ValueError, TypeError):
            pass

    if max_price:
        try:
            packages = packages.filter(price__lte=int(max_price))
        except (ValueError, TypeError):
            pass

    if duration:
        try:
            packages = packages.filter(days=int(duration))
        except (ValueError, TypeError):
            pass


    context = {
        'packages': packages,
        'query': query,
        'total_results': packages.count(),
        'hero': hero,
        'weather': weather
    }
    return render(request, 'search_results.html', context)


def my_bookings(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please login to view your bookings.')
        return redirect('login')

    bookings = BookingPackage.objects.all().order_by('-created_at')
    hero = HeroSection.objects.first()
    has_bookings = bookings.exists()  # efficient check

    return render(request, 'my_bookings.html', {
        'bookings': bookings,
        'has_bookings': has_bookings,
        'hero':hero
    })


def cancel_booking(request, booking_id):
    """Cancel a booking"""
    booking = get_object_or_404(BookingPackage, id=booking_id)

    if request.method == 'POST':
        if booking.status == 'completed':
            messages.error(request, 'Completed bookings cannot be cancelled.')
        elif booking.status == 'cancelled':
            messages.info(request, 'This booking is already cancelled.')
        else:
            booking.status = 'cancelled'
            booking.save()
            messages.success(request, 'Booking cancelled successfully.')

    return redirect('my_bookings')


