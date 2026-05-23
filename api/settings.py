import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "insecure-dev-key-change-in-production")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "corsheaders",
    # Local
    "app.authentication",
    "app.items",
    "app.users",
    "app.notifications",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "api.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "api.wsgi.application"

# Database
import dj_database_url
DATABASES = {
    "default": dj_database_url.config(default=os.getenv("DATABASE_URL"), conn_max_age=600, conn_health_checks=True)
}

AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# DRF
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# SimpleJWT
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "SIGNING_KEY": os.getenv("JWT_SECRET", SECRET_KEY),
}

# Swagger
SPECTACULAR_SETTINGS = {
    "TITLE": "Django API",
    "VERSION": "1.0.0",
    "DESCRIPTION": "REST API with Django + DRF + PostgreSQL",
    "SECURITY": [{"BearerAuth": []}],
}

# CORS
CORS_ALLOW_ALL_ORIGINS = True

# App
APPEND_SLASH = False
