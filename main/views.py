from rest_framework import generics
from rest_framework.permissions import AllowAny

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
    permission_classes = [AllowAny]


class LogListApiView(generics.ListCreateAPIView):
    """ get a list of logs related to the current user """
    serializer_class = LogSerializer
    
    def get_permissions(self):
        #allow unauthenticated access for POST requests
        if(self.request.method.upper() == "POST"):
            return [AllowAny()]
        return super().get_permissions()

    def get_queryset(self):
        user = self.request.user
        return Log.objects.filter(device__user=user)