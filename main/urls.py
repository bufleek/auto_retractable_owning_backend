from django.urls import path

from main.views import DeviceDetailApiView, DeviceListApiView, LogListApiView

urlpatterns = [
    path("devices/", DeviceListApiView.as_view()),
    path("devices/<str:serial_no>/", DeviceDetailApiView.as_view()),
    path("logs/", LogListApiView.as_view()),
]