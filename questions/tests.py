from unittest.mock import patch
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from mixer.backend.django import mixer
import pytest


pytestmark = pytest.mark.django_db
