from .base import *  # pylint: disable=wildcard-import, unused-wildcard-import

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar', )


# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions', )

try:
    from .development_local import *  # pylint: disable=wildcard-import, unused-wildcard-import
except ImportError:
    pass
