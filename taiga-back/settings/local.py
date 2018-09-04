from .common import *


MEDIA_URL = "http://localhost:9001/media/"
STATIC_URL = "http://localhost:9001/static/"
SITES["api"]["scheme"] = 'http'
SITES["api"]["domain"] = "localhost:9001"
SITES["front"]["scheme"] = 'http'
SITES["front"]["domain"] = "localhost:8000"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'taiga',
        'USER': 'taiga',
        'PASSWORD': 'taigapass',
        'HOST': 'postgres',
        'PORT': '5432'
    }
}

SECRET_KEY = 'SECRET_KEY'

DEBUG = False
PUBLIC_REGISTER_ENABLED = True

DEFAULT_FROM_EMAIL = "no-reply@example.com"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# CELERY_ENABLED = True

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {
    "url": "amqp://taiga:taigapass@rabbitmq:5672/taiga"}

# Uncomment and populate with proper connection parameters
# for enable email sending. EMAIL_HOST_USER should end by @domain.tld
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_USE_TLS = False
# EMAIL_HOST = "localhost"
# EMAIL_HOST_USER = ""
# EMAIL_HOST_PASSWORD = ""
# EMAIL_PORT = 25

# Uncomment and populate with proper connection parameters
# for enable github login/singin.
# GITHUB_API_CLIENT_ID = "yourgithubclientid"
# GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"
