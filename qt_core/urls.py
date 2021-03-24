from django.contrib import admin
from django.urls import path, include

from qt_auth.views import Register, Login
from qt_payment.views import Payment, StripeWebhook


auth_auth_patterns = [
    path("register", Register.as_view(), name="register-user"),
    path("login", Login.as_view(), name="login-user"),
    path("payment", Payment.as_view(), name="payment-user"),
    path("stripe_webhook", StripeWebhook.as_view(), name="stripe-webhook"),
]

api_patterns = [
    path("auth/", include(auth_auth_patterns)),
]


urlpatterns = [
    path("api/", include(api_patterns)),
    path("admin/", admin.site.urls),
]
