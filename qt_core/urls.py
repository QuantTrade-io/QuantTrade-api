from django.contrib import admin
from django.urls import path, include

from qt_auth.views import Register, Login


auth_auth_patterns = [
    path("register", Register.as_view(), name="register-user"),
    path("login", Login.as_view(), name="login-user"),
]

api_patterns = [
    path("auth/", include(auth_auth_patterns)),
]


urlpatterns = [
    path("api/", include(api_patterns)),
    path("admin/", admin.site.urls),
]
