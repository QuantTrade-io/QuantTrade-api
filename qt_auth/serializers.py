from rest_framework import serializers

from qt.settings import (
    PASSWORD_MIN_LENGTH,
    PASSWORD_MAX_LENGTH,
    FIRST_NAME_MIN_LENGTH,
    FIRST_NAME_MAX_LENGTH,
    LAST_NAME_MIN_LENGTH,
    LAST_NAME_MAX_LENGTH,
)
from qt_auth.validators import is_email_taken_validator, has_subscription_validator

from django.contrib.auth.password_validation import validate_password


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, allow_blank=False)
    password = serializers.CharField(
        min_length=PASSWORD_MIN_LENGTH,
        max_length=PASSWORD_MAX_LENGTH,
        validators=[validate_password],
    )
    first_name = serializers.CharField(
        required=True,
        allow_blank=False,
        min_length=FIRST_NAME_MIN_LENGTH,
        max_length=FIRST_NAME_MAX_LENGTH,
    )
    last_name = serializers.CharField(
        required=True,
        allow_blank=False,
        min_length=LAST_NAME_MIN_LENGTH,
        max_length=LAST_NAME_MAX_LENGTH,
    )
    are_guidelines_accepted = serializers.BooleanField()

    def validate(self, data):
        is_email_taken_validator(data["email"])
        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_blank=False)
    password = serializers.CharField(
        min_length=PASSWORD_MIN_LENGTH, max_length=PASSWORD_MAX_LENGTH
    )

    def validate(self, data):
        has_subscription_validator(data["email"])
        return data
