from django.urls import path

from accounts.views import LoginApiView, SignupApiView

urlpatterns = [
    path("signup/", SignupApiView.as_view()),
    path("login/", LoginApiView.as_view())
]