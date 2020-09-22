from .base import *

DEBUG = False

ADMINS = (
    ('Maria J', 'mmariajessics@gmail.com'),
)

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'postgres',
        'PASSWORD':'mktj2020',
        
    }
}
