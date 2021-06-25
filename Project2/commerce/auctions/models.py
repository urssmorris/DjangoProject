from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
    #customer_id = models.CharField(max_length=100, blank=True, null=True)
