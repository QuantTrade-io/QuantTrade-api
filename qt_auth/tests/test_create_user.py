from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


REGISTER_USER_URL = reverse("register-user")


class RegistraterUserApiTests(TestCase):
    """Test User Registration API"""

    def setUp(self):
        self.client = APIClient()

    def test_registration_success(self):
        """
        Test creating a user.
        Should return 201.
        """
        payload = {
            "email": "test@test.com",
            "password": "test123123",
            "first_name": "Test",
            "last_name": "Test",
            "are_guidelines_accepted": True,
        }
        res = self.client.post(REGISTER_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_first_name_required(self):
        """
        Test creating a user without a first name.
        Should return 400 if there is no first name.
        """
        payload = {
            "email": "test@test.com",
            "password": "test123123",
            "first_name": "",
            "last_name": "Test",
            "are_guidelines_accepted": True,
        }
        res = self.client.post(REGISTER_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_last_name_required(self):
        """
        Test creating a user without a last name.
        Should return 400 if there is no last name.
        """
        payload = {
            "email": "test@test.com",
            "password": "test123123",
            "first_name": "Test",
            "last_name": "",
            "are_guidelines_accepted": True,
        }
        res = self.client.post(REGISTER_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_email_required(self):
        """
        Test creating a user without an email.
        Should return 400 if there is no email.
        """
        payload = {
            "email": "",
            "password": "test123123",
            "first_name": "Test",
            "last_name": "Test",
            "are_guidelines_accepted": True,
        }
        res = self.client.post(REGISTER_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_required(self):
        """
        Test creating a user without a password.
        Should return 400 if there is no password.
        """
        payload = {
            "email": "test@test.com",
            "first_name": "Test",
            "last_name": "Test",
            "are_guidelines_accepted": True,
        }
        res = self.client.post(REGISTER_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
