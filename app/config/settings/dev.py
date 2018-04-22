from .base import *

import_secrets()

DEBUG = True
WSGI_APPLICATION = 'config.wsgi.dev.application'

# Static
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(ROOT_DIR), 'foodfly_media')
