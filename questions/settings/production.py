from .base import *  # pylint: disable=wildcard-import, unused-wildcard-import

DEBUG = False

try:
    from .production_local import *  # pylint: disable=wildcard-import
except ImportError:
    pass
