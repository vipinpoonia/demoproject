from .common import *

DEBUG = False

# Db settings for production
SECRET_KEY = 'asfjasf-asfjasfj'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'HOST': '',
        'PORT': 5432,
        'USER': '',
        'PASSWORD': '',
    }
}
