from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


REGISTER_USER_URL = reverse("register-user")
LOGIN_USER_URL = reverse("login-user")


class LoginUserApiTests(TestCase):
    """Test User Login API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_without_suscription(self):
        """
        Test login a user without a subscription.
        Should return 400 if user has no subscription.
        """
        register_payload = {
            "email": "test@test.com",
            "password": "test123123",
            "first_name": "Test",
            "last_name": "Test",
            "are_guidelines_accepted": True,
        }
        self.client.post(REGISTER_USER_URL, register_payload)

        # user = get_user_model().objects.filter(username=register_payload["email"])

        login_payload = {"email": "test@test.com", "password": "test123123"}

        login_res = self.client.post(LOGIN_USER_URL, login_payload)
        self.assertEqual(login_res.status_code, status.HTTP_400_BAD_REQUEST)
