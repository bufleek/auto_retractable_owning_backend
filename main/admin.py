from django.contrib import admin

from main.models import Device

# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ["serial_no", "retraction_status", "user"]

admin.site.register(Device, DeviceAdmin)
