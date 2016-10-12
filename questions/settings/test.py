from .base import *  # pylint: disable=wildcard-import, unused-wildcard-import

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'memory',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
DJMOODLE_TRACK_USERS = False
LOGGING = {}

DJSLACK_TOKEN = '12345'
DJSLACK_CHANNEL = '#exceptions'
DJSLACK_USERNAME = 'Exception service'
