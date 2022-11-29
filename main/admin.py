from django.contrib import admin

from main.models import Device, Log

# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ["serial_no", "retraction_status", "user"]

class LogsAdmin(admin.ModelAdmin):
    list_display = ["device", "title", "message", "created_at"]

admin.site.register(Device, DeviceAdmin)
admin.site.register(Log, LogsAdmin)
