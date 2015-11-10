"""
Django settings for site_des_eleves project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&d3ykoj75pkdv_q^4%ens@047+qi^_^379rg#!o%zg1j=pmwi&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'notifications',
    'accounts',
    'poll',
    'events',
    'webmail',
    'bde',
    'carshare',
    'news',
    'shop',
    'pizza',
    'help',
    'permissions',
    'photo',
    'enibar',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'notifications.middleware.ReadOnVisit',
)

ROOT_URLCONF = 'site_des_eleves.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'notifications.context_processors.check_notifications',
                'bde.context_processors.bde_member',
            ],
        },
    },
]

WSGI_APPLICATION = 'site_des_eleves.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sde',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'collected_static'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/medias')
MEDIA_URL = '/static/medias/'

# Authentification backend

AUTHENTICATION_BACKENDS = (
    'accounts.backends.NormalAuth',
    'accounts.backends.ImapAuth',
    'django.contrib.auth.backends.ModelBackend'
)

LOGIN_URL = '/accounts/login'


# Mails

EMAIL_HOST=""
EMAIL_PORT=587
EMAIL_HOSt_USER=""
EMAIL_HOST_PASSWORD=""
EMAIL_USE_TLS=True



# Permissions
PERM_ENABLE_WHITELIST = True
PERM_WHITELIST = {
    'auth': [
        'add_group',
        'delete_group',
        'change_permission',
    ],

    'bde': [
        'change_contributor',
    ],

    'accounts': [
        'manage_account_request',
    ],

    'carshare': [
        'change_announcement',
        'delete_announcement',
        'delete_registration',
    ],

    'events': [
        'add_event',
        'change_event',
        'delete_event',
        'access_list',
        'manage_entries',
    ],

    'news': [
        'delete_comment',
        'add_news',
        'change_news',
        'delete_news',
    ],

    'poll': [
        'add_poll',
        'change_poll',
        'delete_poll',
    ],

}


# Application settings
BDE_GROUP_NAME = 'BDE'

try:
    from .local_settings import *
except:
    pass

import sys
import os

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/tmp/mysql_sde.socket',
            'NAME': 'sde_tests',
            'USER': 'root',
            'PASSWORD': "",
            'PORT': 4569,

        }
    }

