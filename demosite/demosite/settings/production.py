from .common import *

DEBUG = False
ALLOWED_HOSTS = ['*']

SECRET_KEY = secrets.value("SECRET_KEY")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': secrets.value("DEFAULT_DB_NAME"),
        'HOST': secrets.value("DEFAULT_DB_HOST"),
        'PORT': 5432,
        'USER': secrets.value("DEFAULT_DB_USER"),
        'PASSWORD': secrets.value("DEFAULT_DB_PASSWORD"),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}