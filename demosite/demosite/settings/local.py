from .common import *

DEBUG = True
ALLOWED_HOSTS = ['*']

SECRET_KEY = secrets.value("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'PORT': 5432,
        'NAME': 'demosite',
        'USER': 'demouser',
        'PASSWORD': 'd3m0d3m0',
    }
}
