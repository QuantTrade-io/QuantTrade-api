import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    """
    Custom user model to change behaviour of the default user mode,
    such as validation and required fields.
    """
    username = None
    email = models.EmailField(unique=True, null=False, blank=False)
    email_verified = models.BooleanField(default=False)
    guidelines_accepted = models.BooleanField(default=False)
    subscription_paid = models.BooleanField(default=False)
    # uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
