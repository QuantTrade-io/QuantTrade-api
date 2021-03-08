import uuid

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """
    Custom user model to change behaviour of the default user mode,
    such as validation and required fields.
    """

    username = models.EmailField(null=False, blank=False, unique=True)
    guidelines_accepted = models.BooleanField(default=False)
    paid_subscription = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.username

    @classmethod
    def create_user(cls, email, password, first_name, last_name, guidelines_accepted):

        if not guidelines_accepted:
            raise ValidationError(
                _("You must confirm the guidelines to create an account.")
            )
        new_user = cls.objects.create_user(
            username=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            guidelines_accepted=guidelines_accepted,
        )

        return new_user

    @classmethod
    def is_email_taken(cls, username):
        try:
            User.objects.get(username=username)
            return True
        except User.DoesNotExist:
            return False

    @classmethod
    def has_subscription(cls, username):
        return User.objects.get(username=username).paid_subscription
