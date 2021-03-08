from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from qt_auth.models import User


def is_email_taken_validator(username):
    if User.is_email_taken(username):
        raise ValidationError(
            _("An account for the email already exists."),
        )


def has_subscription_validator(username):
    subscription = User.has_subscription(username)
    if subscription is False:
        raise ValidationError(
            ({"error": "You need a subscription to get access to the web app"})
        )
    else:
        return True
