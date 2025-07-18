import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = "django-insecure-#889hc07bow(1szinf7&)!oc7=d$wcwcf$6qz$^3m--omry#hm"

DEBUG = True

ALLOWED_HOSTS = ["volshebnikstore.pythonanywhere.com", "127.0.0.1", "volshebnik.uz"]

CSRF_TRUSTED_ORIGINS = ["https://volshebnik.uz"]

INSTALLED_APPS = [
    # admin
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history",
    # external
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "constance",
    "nested_inline",
    "core.apps.main.apps.MainConfig",
    "core.apps.news.apps.NewsConfig",
    "core.apps.services.apps.ServicesConfig"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.shop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
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

WSGI_APPLICATION = "core.shop.wsgi.application"

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        # 'USER': DB_USER,
        # 'PASSWORD': DB_PASSWORD,
        # 'HOST': DB_HOST,
        # 'PORT': DB_PORT,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True

STATIC_URL = "site/static/"
STATIC_ROOT = BASE_DIR / "main/static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

UNFOLD = {
    "SITE_TITLE": "Volshebnik-shop",
    "SITE_HEADER": "Volshebnik-shop",
    "SITE_SUBHEADER": "admin-panel",
}

SERVICE_ACCOUNT_EMAIL = (
    "volshebnik-content@volshebnik-content-table.iam.gserviceaccount.com"
)

GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/1ovrfMEvJWpkttXBq9cp_i2aLJcGWS2X8vQF_bfStuZA/edit?gid=1128242186#gid=1128242186"
TABLE_ID = "1ovrfMEvJWpkttXBq9cp_i2aLJcGWS2X8vQF_bfStuZA"
CORS_ALLOW_ALL_ORIGINS = True

IMAGES_PATH = os.getenv("IMAGES_PATH")
EXCEL_FILENAME = os.getenv("EXCEL_FILENAME")

CONSTANCE_CONFIG = {
    'SITE_DESCRIPTION': (
        'Волшебный магазин товаров для праздников, уюта и вдохновения. Доставка по всему Казахстану и СНГ.', ''),
    'PHONE_NUMBER': ('+7 (707) 123-45-67', ''),
    'EMAIL': ('info@volshebnik.uz', ''),
    'ADDRESS': ('г. Алматы, ул. Сказочная, 1', ''),
    'TELEGRAM_URL': ('https://t.me/joinchat/AAAAAFfIyzwGkO8X8CDnvA', ''),
    'INSTAGRAM_URL': ('https://www.instagram.com/volshebnik.uz', ''),
    'FACEBOOK_URL': ('https://www.facebook.com/Volshebnik.uz', '')
}
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
