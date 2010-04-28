DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'

MEDIA_ROOT = ''
MEDIA_URL = ''

SECRET_KEY = 'x#o7f-9-5q2vwcmv+v(@^@w)8men@2135%ip2u10-9^ebx&e8g'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

ROOT_URLCONF = 'test_app.urls'

INSTALLED_APPS = (
    'test_app',
    'django_assets',
)
