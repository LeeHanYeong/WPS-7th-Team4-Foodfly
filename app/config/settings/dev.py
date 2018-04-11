from .base import *

secrets = json.loads(open(SECRET_DEV).read())
for key, value in secrets.items():
    setattr(sys.modules[__name__], key, value)

DEBUG = True
ALLOWED_HOSTS = [
    '.localhost',
    '127.0.0.1',
    '.lhy.kr',
]
WSGI_APPLICATION = 'config.wsgi.dev.application'

# Static
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
