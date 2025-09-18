import os
from pathlib import Path
from dotenv import load_dotenv

# BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================================
# DJANGO SECRET KEY
# ==============================================================
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "unsafe-default-key")
load_dotenv()
# ==============================================================
# DEBUG
# ==============================================================
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "*",
    ".vercel.app",
    "www.royalcrestindia.in",
    "royalcrestindia.in",
]

# ==============================================================
# INSTALLED APPS
# ==============================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom apps
    'home',
    'gallery',

    # AWS & storage
    'storages',
]

# ==============================================================
# MIDDLEWARE
# ==============================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # WhiteNoise for static files
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'royalcrest.urls'

# ==============================================================
# TEMPLATES
# ==============================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ==============================================================
# WSGI
# ==============================================================
WSGI_APPLICATION = 'royalcrest.wsgi.application'

# ==============================================================
# DATABASE (PostgreSQL)
# ==============================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'royalcrestdb'),
        'USER': os.environ.get('DB_USER', 'royalcrestuser'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'password123'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# ==============================================================
# PASSWORD VALIDATION
# ==============================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==============================================================
# LANGUAGE & TIMEZONE
# ==============================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ==============================================================
# STATIC FILES
# ==============================================================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise for static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ==============================================================
# AWS S3 MEDIA STORAGE
# ==============================================================

# Get AWS credentials from environment variables
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "royalcrest-media")
AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME", "ap-southeast-2")

# Custom domain for S3 bucket
AWS_S3_CUSTOM_DOMAIN = f"royalcrest-media.s3.amazonaws.com"

# Use S3 for media storage
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# Media URL points to S3
MEDIA_URL = f"https://royalcrest-media.s3.ap-south-1.amazonaws.com/media/"

# Optional: Prevent overwriting files with same name
AWS_S3_FILE_OVERWRITE = False

# ==============================================================
# DEFAULT PRIMARY KEY FIELD TYPE
# ==============================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
