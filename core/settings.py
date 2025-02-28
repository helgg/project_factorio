from pathlib import Path
import os # configuração necessária helgg

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent 
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # configuração necessária helgg


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qjn8kc%j(mz6w08+@xbg8jm7r+52c3boe11clwzq89odm55#05'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # custom apps
    'app',
    'authentication',

    # third party apps
    'social_django',
    'tailwind',
    'theme',
    'django_browser_reload'
]

TAILWIND_APP_NAME = 'theme'

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '78119813743-hr6s7cs03b1mnlneflq9q0v91b3ppv5b.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

ROOT_URLCONF = 'core.urls'

TEMPLATE_DIR = os.path.join(CORE_DIR, "core/templates") # configuração necessária helgg

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,], # configuração necessária helgg
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators


AUTH_USER_MODEL = 'authentication.User'


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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/' 
STATIC_ROOT = os.path.join(CORE_DIR, 'static/') 

TAILWIND_CSS_PATH = 'css/dist/styles.css'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core/static'),
    os.path.join(BASE_DIR, 'theme/static'),
] 
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(CORE_DIR, 'media/') 

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# https://django-jazzmin.readthedocs.io/configuration/
JAZZMIN_SETTINGS = {
    "site_title": "Administração",
    "site_header": "Painel Administrativo",
    "site_brand": "Project Factorio",
    "site_logo": "images.jpeg",
    "welcome_sign": "Bem-vindo ao Admin",
    "copyright": "Project Factorio © 2025",
    "search_model": ["auth.User"],  # pra colocar barras de pesquisa das tabelas
    "user_avatar": 'app.Profile.profile_photo',  # TODO: estou tentando colocar imagen do profile aqui mas...
    "topmenu_links": [
        {"name": "Home", "url": "app:home", "permissions": ["auth.view_user"]},
        {"name": "GitHub", "url": "https://github.com/helgg/project_factorio", "new_window": True},
    ],
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.User"}
    ],
    "icons": {
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "app.Blog": "fas fa-database",
        "app.Profile": "fas fa-database",
        "app.BlogView": "fas fa-database",
    },
}
