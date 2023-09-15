"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gc3t3bt60yrj4e2&ka7rhjasjhd047l8(n#@347dxm&mk-v+sn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 'django-filters',
    'rest_framework',
    
    'core',
    
    # DJOSER DRF AUTH
    'djoser',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'global/static/')]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
        # 'rest_framework.permissions.IsAuthenticated'
    ],
    
    'DEFAULT_THROTTLE_CLASSES': [
        # ANONYMOUS THROTTLE
        'rest_framework.throttling.AnonRateThrottle',
        # AUTHENTICATED THROTTLE
        'rest_framework.throttling.UserRateThrottle',
    ],
    
    'DEFAULT_THROTTLE_RATES':{
        'anon': '20/min',
        'user': '100/min'
    },
    
    # PAGINATION
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10
}

# JWT CONFIGS
# SIMPLE_JWT = {
#     'AUTH_HEADERS_TYPES': ['Bearer'],
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=1)
# }

JAZZMIN_SETTINGS = {
    "site_title": "LabManager",
    "welcome_sign": "Welcome back",
    "site_header": "ETS",
    "site_brand": "ETS",
    "copyright": "https://github.com/socksOnly",
    # "site_logo": "images/logo2.svg",
}

JAZZMIN_UI_TWEAKS = { 
    "navbar_small_text": False, 
    "footer_small_text": False, 
    "body_small_text": False, 
    "brand_small_text": False, 
    "brand_colour": "navbar-primary", 
    "accent": "accent-teal", 
    "navbar": "navbar-dark", 
    "no_navbar_border": False, 
    "navbar_fixed": False, 
    "layout_boxed": False, 
    "footer_fixed": False, 
    "sidebar_fixed": False, 
    "sidebar": "sidebar-dark-info", 
    "sidebar_nav_small_text": False, 
    "sidebar_disable_expand": False, 
    "sidebar_nav_child_indent": False, 
    "sidebar_nav_compact_style": False, 
    "sidebar_nav_legacy_style": False, 
    "sidebar_nav_flat_style": False, 
    "theme": "cyborg", 
    # "theme": "solar", 
    "dark_mode_theme": 'darkly', 
    "button_classes": { 
        "primary": "btn-primary", 
        "secondary": "btn-secondary", 
        "info": "btn-info", 
        "warning": "btn-warning", 
        "danger": "btn-danger", 
        "success": "btn-success", 
    }, 
}