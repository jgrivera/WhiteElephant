import os

#from configurations import Configuration

#class Dev(Configuration):
#   DEBUG = True

DEBUG = False


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rha7*we-io_dbhnf$k)%wum_i=-fct9+n^j+@5j9p*$z01lzj1'

# # List of callables that know how to import templates from various sources.
# TEMPLATE_LOADERS = (
#     ('django_mobile.loader.CachedLoader', (
#         'django_mobile.loader.Loader',
#         'django.template.loaders.filesystem.Loader',
#         'django.template.loaders.app_directories.Loader',
#     )),
# )



ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'game.apps.GameConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.amazon',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'django_mobile',
]

LOGIN_REDIRECT_URL = ('/')
SITE_ID = 2

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',
]

ROOT_URLCONF = 'WhiteElephant.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django_mobile.context_processors.flavour',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            'loaders': [
                'django_mobile.loader.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

TEMPLATE_LOADERS = TEMPLATES[0]['OPTIONS']['loaders']

WSGI_APPLICATION = 'WhiteElephant.wsgi.application'

# Database
#DATABASES = {
#   'default': {
#       'ENGINE': 'django.db.backends.sqlite3',
#       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#   }
#}

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         #'ENGINE': 'mysql.connector.django',
         'NAME': 'mydb',
         'USER': 'root',
         'PASSWORD': 'root',
         'HOST': 'ec2-35-161-82-43.us-west-2.compute.amazonaws.com',
        'PORT': '3306',
     }
 }

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
         {'SCOPE': ['email'],
          'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
          'METHOD': 'oauth2',
          'LOCALE_FUNC': 'en-US'}}

# Password validation
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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = '/opt/WhiteElephant/WhiteElephant/game/static'
STATIC_URL = '/game/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

try:
    from .local_settings import *
except ImportError:
    pass
