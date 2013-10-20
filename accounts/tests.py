"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth import login
from django.http import HttpRequest

from django.contrib.sessions.models import SessionStore
from accounts.models import User

class MinimalUserModelTest(TestCase):

    def test_login_a_user(self):
        request = HttpRequest()
        request.session = SessionStore()
        user = User()
        user.backend = '' # no idea what this is
        login(request, user)
