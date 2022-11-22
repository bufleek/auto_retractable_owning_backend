from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        fields = ["id", "username", "first_name", "last_name", "email"]
        model = User