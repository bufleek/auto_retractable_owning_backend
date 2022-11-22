from rest_framework import serializers

from accounts.serializers import UserSerializer
from main.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        fields = ["id", "user"]
        model = Device