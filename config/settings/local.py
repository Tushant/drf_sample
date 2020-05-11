from django.core.management.utils import get_random_secret_key

from .base import *  # noqa
from .base import env

DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default=get_random_secret_key(),
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
