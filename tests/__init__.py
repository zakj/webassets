# Configure Django for our tests. This can't be within a ``setup_package``
# function, or it will most likely only be executed after the django-assets
# conf module is imported, which then initializes itself based on an
# empty Django settings object.
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_app.settings'


def setup_package():
    # Unless explicitely tested, we don't want to use the cache.
    from django_assets.conf import settings
    settings.ASSETS_CACHE = False

    # We'd like to have some other settings be the default for
    # these tests, without relying on the values given in the
    # settings.py file of the test app, so set them here - some
    # tests expect to run in that environment.
    settings.DEBUG = False