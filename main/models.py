
from django.db import models

from accounts.models import User


class DeviceRetractionStatus(models.IntegerChoices):
    RETRACTED = 0
    EXPANDED = 1


class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    serial_no = models.CharField(max_length=25, null=False, blank=False, unique=True)
    retraction_status = models.IntegerField(choices=DeviceRetractionStatus.choices, default=DeviceRetractionStatus.RETRACTED.value)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "devices"


class Log(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "logs"