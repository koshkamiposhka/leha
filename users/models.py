from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, unique=True, null=False, blank=True)
    telegram_id = models.CharField(max_length=50, unique=True, null=False, blank=True)  

    def __str__(self):
        return self.username