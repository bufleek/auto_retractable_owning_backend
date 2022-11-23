
from django.db import models

from accounts.models import User


class DeviceRetractionStatus(models.IntegerChoices):
    RETRACTED = 0
    EXPANDED = 1

class OnOffStatus(models.IntegerChoices):
    ON=1
    OFF=0


class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    serial_no = models.CharField(max_length=25, null=False, blank=False, unique=True)
    retraction_status = models.IntegerField(choices=DeviceRetractionStatus.choices, default=DeviceRetractionStatus.RETRACTED.value)
    ldr_threshold = models.DecimalField(max_digits=10,decimal_places=4, null=True, blank=True)
    ldr_status = models.IntegerField(choices=OnOffStatus.choices, default=OnOffStatus.OFF)
    rain_sensor_threshold = models.DecimalField(max_digits=10,decimal_places=4, null=True, blank=True)
    rain_sensor_status = models.IntegerField(choices=OnOffStatus.choices, default=OnOffStatus.OFF)
    motion_sensor_threshold = models.DecimalField(max_digits=10,decimal_places=4, null=True, blank=True)
    motion_sensor_status = models.IntegerField(choices=OnOffStatus.choices, default=OnOffStatus.OFF)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "devices"


class Log(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "logs"