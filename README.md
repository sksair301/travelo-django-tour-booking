<div align="center">

# **Travelo – Django Tour & Travel Booking Website**

**Travelo** is a modern, fully responsive Django-based travel and tour booking platform.  
It offers dynamic content management through Django Admin for hero banners, services, hotels, and galleries.  
Designed and enhanced by animations for a delightful travel experience.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](#)
[![Django](https://img.shields.io/badge/Django-5.x-092E20?logo=django&logoColor=white)](#)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap&logoColor=white)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#)

</div>

##  Features

-  Dynamic Hero Section (editable via admin)
-  Manageable Services (title, icons, background images)
-  Hotel listing & booking cards
-  Interactive gallery (3D tilt & carousel view)
-  About & Contact pages with admin-managed content
-  Fully responsive, mobile-friendly UI
-  Django Admin dashboard for content control
-  Animated transitions & parallax effects

---

## Tech Stack

| Category | Technologies Used |
|-----------|------------------|
| **Backend** | Django 5.x, Python 3.x |
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript |
| **Database** | SQLite3 (default) |
| **Media Handling** | Django `ImageField`, `MEDIA_URL`, `MEDIA_ROOT` |
| **Animations** | AOS.js / Swiper.js / VanillaTilt.js |
| **Version Control** | Git & GitHub |

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/travelo-django-tour-booking.git
   cd travelo-django-tour-booking
2. **Create and Activate a Virtual Environment**
 For Windows:
    ```bash
   python -m venv venv
   venv\Scripts\activate

3. **Install Required Packages**
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt

4. **If you don’t have a requirements.txt yet, create one later using:**
    ```bash
    pip freeze > requirements.txt

5. **Apply Database Migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

6. **Create Superuser (for Admin Access)**
    ```bash
    python manage.py createsuperuser

7. **Run the Development Server**
    ```bash
   python manage.py runserver

8. **Configure Media & Static Files in Settings.py**
    ```bash
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'

    STATIC_URL = '/static/'
    STATICFILES_DIRS = [BASE_DIR / 'static']

## 🖼️ Screenshots

| Homepage | Destinations | Popular Tours |
|-----------|---------------|---------------|
| ![Home](https://github.com/sksair301/travelo-django-tour-booking/blob/788c86416a9a4d61bfd5ef3ee66cb39fe2d1b854/s-1.png) | ![Destinations](https://github.com/sksair301/travelo-django-tour-booking/blob/10e224a4608e7ef7de60f320ec75a2edddcb910e/s-2.png) | ![Popular Tours](https://github.com/sksair301/travelo-django-tour-booking/blob/10e224a4608e7ef7de60f320ec75a2edddcb910e/s-3.png) |

| Tour Packages | Tour Detail Page | Hotels | Hotel Detail Page |
|----------------|------------------|---------|-------------------|
| ![Packages](https://github.com/sksair301/travelo-django-tour-booking/blob/10e224a4608e7ef7de60f320ec75a2edddcb910e/s-4.png) | ![Tour Detail](https://github.com/sksair301/travelo-django-tour-booking/blob/10e224a4608e7ef7de60f320ec75a2edddcb910e/s-5.png) | ![Hotels](https://github.com/sksair301/travelo-django-tour-booking/blob/10e224a4608e7ef7de60f320ec75a2edddcb910e/s-6.png) | ![Hotel Detail](https://github.com/sksair301/travelo-django-tour-booking/blob/10e224a4608e7ef7de60f320ec75a2edddcb910e/s-7.png) |




  





