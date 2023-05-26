from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    phone = PhoneNumberField()
    def __str__(self):
        return self.email
        return self.phone
