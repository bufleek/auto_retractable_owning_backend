from rest_framework import serializers

from main.models import Device, Log


class DeviceSerializer(serializers.ModelSerializer):
    serial_no = serializers.ReadOnlyField()

    class Meta:
        exclude = ["user", "created_at"]
        model = Device


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Log