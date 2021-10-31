import os

from .base import *

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
