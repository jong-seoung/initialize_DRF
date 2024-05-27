"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(env_file=os.path.join(BASE_DIR, ".env"))
SECRET_KEY = env("SECRET_KEY")

# Application definition

LOCAL_APPS = ["core", "api.models.users", "api.models.boards"]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "drf_yasg",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "config.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "ko-KR"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = False

# User Model
AUTH_USER_MODEL = "users.User"
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# RestFramework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("core.middlewares.CustomJWTAuthentication",),
    # Response class include renderer method
    # "DEFAULT_RENDERER_CLASSES": [
    #     "core.renderers.CustomRenderer",
    # ],
    "DEFAULT_RENDERER_CLASSES": (
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
        "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    ),
    "DEFAULT_PAGINATION_CLASS": "core.paginations.CustomPagination",
}

AUTHENTICATION_BACKENDS = ("core.backends.CustomJWTBackend",)

# djangorestframework-simplejwt
REST_USE_JWT = True

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=365),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": True,
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Logging

DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"
LOG_FILE_NAME = "local.log" if DEBUG else "pro.log"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_true": {"()": "django.utils.log.RequireDebugTrue"},
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"},
    },
    "formatters": {
        "standard": {"format": "{asctime} [{levelname}] {name} {message}", "style": "{"},
        "django.server": {
            "format": "{asctime} [{levelname}] {name} {message} \n"
            "\t[PID: {process} - {processName}] | [TID: {thread} - {threadName}]",
            "style": "{",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {"level": "INFO", "class": "logging.StreamHandler"},
        "file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            # 'class': 'logging.handlers.TimedRotatingFileHandler',
            "filename": os.path.join(BASE_DIR, f"logs/{LOG_FILE_NAME}"),
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            # 'when': 'midnight',
            # 'interval': 1,
            # 'backupCount': 7,
            "formatter": "standard",
        },
        "error_file": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            # 'class': 'logging.handlers.TimedRotatingFileHandler',
            "filename": os.path.join(BASE_DIR, "logs/errors.log"),
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            # 'when': 'midnight',
            # 'interval': 1,
            # 'backupCount': 7,
            "formatter": "django.server",
        },
    },
    "loggers": {
        "": {"handlers": ["console", "file", "error_file"], "level": "DEBUG", "propagate": True},
        "django": {"handlers": ["console", "file", "error_file"], "level": "DEBUG", "propagate": False},
    },
}