from decouple import config
from dj_database_url import parse as db_url
from unipath import Path
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = Path(__file__).parent

#import cloudinary
#import cloudinary.uploader
#import cloudinary.api

DEFAULT_FROM_EMAIL = "site.motok@gmail.com"
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER="site.motok@gmail.com"
EMAIL_HOST_PASSWORD=config('PASS_EMAIL')
EMAIL_USE_TLS=True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '.herokuapp.com']

SOUTH_TESTS_MIGRATE = False


# Application definition

INSTALLED_APPS = (
    'suit',
	'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'widget_tweaks',
	'south',
	'cloudinary',
	'tinymce',
	'chuckchurros.core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'chuckchurros.urls'

WSGI_APPLICATION = 'chuckchurros.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
        'default': config(
			'DATABASE_URL',
            default='sqlite:///' + BASE_DIR.child('db.sqlite3'),
			cast=db_url
			),
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = BASE_DIR.child('staticfiles')
STATIC_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

SUIT_CONFIG = {
    'SEARCH_URL': '/admin/user',
    # Parameter also accepts url name
    'SEARCH_URL': 'admin:auth_user_changelist',

    # Set to empty string if you want to hide search from menu
    'SEARCH_URL': ''
}

'''
AUTHENTICATION_BACKENDS = (
	'eventex.myauth.backends.EmailBackend',
	'django.contrib.auth.backends.ModelBackend',
)
'''

#AUTH_USER_MODEL = 'myauth.User'

TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",    
	'plugins' : "pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,wordcount,advlist,autosave",
	'theme_advanced_buttons1' : "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect,fullscreen,code",
	'theme_advanced_buttons2' : "cut,copy,paste,pastetext,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,|,insertdate,inserttime,preview,|,forecolor,backcolor",
	'theme_advanced_buttons3' : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl",
	'theme_advanced_toolbar_location' : "top",
	'theme_advanced_toolbar_align' : "left",
	'theme_advanced_statusbar_location' : "bottom",
	'theme_advanced_resizing' : 'true',	
	'width': '700',
	'height': '400'
}
#'theme_advanced_buttons3_add': "|,spellchecker",
#'plugins': "spellchecker",


CLOUDINARY = {
    'cloud_name' : 'fighter',
    'api_key' : config('CLOUDINARY_KEY'),
    'api_secret':config('CLOUDINARY_SECRECT')
}