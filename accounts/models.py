from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class Log(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


class User(AbstractUser):
    pass


