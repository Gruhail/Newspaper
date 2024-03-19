
import logging
import os.path
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-_$q8-n&3ln5-mt*#p32%51^4d(97mmwact2*q@_kun+5$h85ay'


DEBUG = True

ALLOWED_HOSTS = []





INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',
    'news.apps.NewsConfig',
    'subscriptions.apps.SubscriptionsConfig',
    'django_filters',
    'django_apscheduler',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'News_Portal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'news/templates/news')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'News_Portal.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



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



LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = "/news"


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]



ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'

EMAIL_PORT = 465
"""
Порт, на который почтовый сервер принимает письма, называется почтовым портом.
Один из самых распространенных почтовых портов - это порт 25, который
используется для передачи электронной почты
по протоколу SMTP (Simple Mail Transfer Protocol).
Однако, существуют и другие почтовые порты, такие как порт 587,
который используется для SMTP с шифрованием TLS (Transport Layer Security),
и порт 465,
который используется для SMTP с шифрованием SSL (Secure Sockets Layer).
Использование конкретного почтового порта зависит от настроек и требований
почтового сервера.
"""
EMAIL_HOST_USER = "Example"

EMAIL_HOST_PASSWORD = "zuqvkobqbkixymje"

EMAIL_USE_TLS = False


EMAIL_USE_SSL = True


DEFAULT_FROM_EMAIL = "Example@yandex.ru"


SERVER_EMAIL = "Example@yandex.ru"

ADMINS = (
    ('ADMIN', 'ADMIN@zhiza.net'),
    ('admin', 'admin@mail.com'),
)

EMAIL_SUBJECT_PREFIX = 'News Portal'

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Moscow'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),

    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {

        'custom-format-D': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },

        'custom-format-I': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },

        'custom-format-W': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },

        'custom-format-EC': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
        'email_format': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
    },
    'filters': {
        'If_Debug_False': {

            '()': 'django.utils.log.RequireDebugFalse'
        },
        "If_Debug_True": {
            "()": "django.utils.log.RequireDebugTrue",
        }

    },
    'handlers': {

        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'custom-format-D',
            'level': 'DEBUG',
            'filters': ['If_Debug_True']
        },
        "console_error": {
            "class": "logging.StreamHandler",
            "formatter": "custom-format-W",
            "filters": ['If_Debug_True'],
            "level": "ERROR",
            },
        "console_warning": {
            "class": "logging.StreamHandler",
            "formatter": "custom-format-EC",
            "filters": ['If_Debug_True'],
            "level": "WARNING",
            },

        'general_file': {
            'class': 'logging.FileHandler',
            'filename': 'logs/general.log',
            'level': 'INFO',
            'formatter': 'custom-format-I',
            'filters': ['If_Debug_False']
        },

        'errors_file': {
            'class': 'logging.FileHandler',
            'filename': 'logs/errors.log',
            'level': 'ERROR',
            'formatter': 'custom-format-EC'
        },

        'security_file': {
            'class': 'logging.FileHandler',
            'filename': 'logs/security.log',
            'level': 'INFO',
            'formatter': 'custom-format-W'
        },

        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            'formatter': 'email_format'
        },
    },
    'loggers': {
        'django': {
            'handlers': [
                'console',
                'general_file',
                'errors_file',
                'mail_admins'
            ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errors_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
        'django.server': {
            'handlers': ['errors_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
        'django.template': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['security_file', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

logger = logging.getLogger("django")
