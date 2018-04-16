from .base import *

import_secrets()

DEBUG = True
ALLOWED_HOSTS = [
    '.localhost',
    '127.0.0.1',
    '.lhy.kr',
]
WSGI_APPLICATION = 'config.wsgi.local.application'

# Static
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
