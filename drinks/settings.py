# Django settings for drinks project.

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('boubekki', 'boubekki@enseirb.fr'),
)

ROOT_PATH = "/home/amirouche/Desktop/drinks-project"
ROOT_URL = "http://localhost:8000"

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', '' or 'oracle'.
DATABASE_NAME = '../mydb.sqlite'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'Europe/Paris'

LANGUAGE_CODE = 'en-uk'

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = os.path.join(ROOT_PATH, "media")

MEDIA_URL = os.path.join(ROOT_URL, "media")

ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = 'kr-l13!sq$k1n^6tvgjy$#w(^pt4ma8&#s12-6hlt+=8$7gw(x'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'drinks.urls'

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admindocs',
    'django.contrib.admin',
    'mydrinks',
)
