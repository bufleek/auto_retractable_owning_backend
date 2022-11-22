from rest_framework import generics

from main.models import Device, Log
from main.serializers import DeviceSerializer, LogSerializer


class DeviceListApiView(generics.ListAPIView):
    """ get a list of devices assigned to the current user """
    serializer_class = DeviceSerializer

    def get_queryset(self):
        user = self.request.user
        return Device.objects.filter(user=user)

class DeviceDetailApiView(generics.RetrieveUpdateAPIView):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()
    lookup_field = "serial_no"


class LogListApiView(generics.ListAPIView):
    """ get a list of logs related to the current user """
    serializer_class = LogSerializer

    def get_queryset(self):
        user = self.request.user
        return Log.objects.filter(device__user=user)