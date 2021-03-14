from rest_framework.exceptions import ValidationError

from qt_auth.models import User


def is_email_taken_validator(username):
    if User.is_email_taken(username):
        raise ValidationError(
            ({"error": "An account for the email already exists."}),
        )


def has_subscription_validator(username):
    subscription = User.has_subscription(username)
    if subscription is False:
        raise ValidationError(
            ({"error": "You need a subscription to get access to the web app"})
        )
    else:
        return True


def password_length_validator(password):
    if password.length <= 10:
        raise ValidationError(({"error": "Password too short"}))
