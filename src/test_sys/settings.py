# -*- coding: utf-8 -*-
"""
Django settings for test_sys project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import ConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l9cavlgzgdr4mx#fv_lf8kstk$k1y*^jvoq^7@p@in1l!wk+9*'

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
)

ROOT_URLCONF = 'test_sys.urls'

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

WSGI_APPLICATION = 'test_sys.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# задаем имя дефолтного конфига
DEFAULT_CONFIG_NAME = 'test_sys.conf'

# инициализируем конфигпарсер
conf = ConfigParser.ConfigParser()

# отдаем путь до конфига из виртуального окружения
config_path = os.environ.get('TESTSYS_CONFIG_PATH')

# ругаемся
if not config_path:
    raise Exception(
        u'Sorry! There is no environment variable "TESTSYS_CONFIG_PATH"')

# ругаемся
if not os.path.exists(config_path) or not os.path.isdir(config_path):
    raise Exception(
        u'The path specified in environment varible "TESTSYS_CONFIG_PATH"',
        u'doesn\'t exist or it is not a directory!')

# ругаемся
config_path += DEFAULT_CONFIG_NAME
if not os.path.exists(config_path) or os.path.isdir(config_path):
    raise Exception(
        u'Config file at path {0} does not exist!'.format(config_path))

# если не попали на ругачку, читаем конфиг
conf.read(config_path)

DATABASES = {
    'default': {
        'ENGINE': conf.get('default_database', 'DATABASE_ENGINE'),
        'NAME': conf.get('default_database', 'DATABASE_NAME'),
        'USER': conf.get('default_database', 'DATABASE_USER'),
        'PASSWORD': conf.get('default_database', 'DATABASE_PASSWORD'),
        'HOST': conf.get('default_database', 'DATABASE_HOST'),
        'PORT': conf.get('default_database', 'DATABASE_PORT')
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
