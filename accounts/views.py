from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.models import User
from accounts.serializers import UserSerializer


class SignupApiView(TokenObtainPairView):
    
    ### perfoms extra validations not included in serializer
    def validate(self, data):
        errors = dict()
        password = data.get("password", None)
        conf_password = data.get("conf_password")
        if password is None or password == "":
            errors["password"] = ["This field may not be null."]
        elif password != conf_password:
            errors["password"] = ["Passwords do not match."]
            errors["conf_password"] = ["Passwords do not match."]
        return errors

    def post(self, request, *args, **kwargs):
        data = {**request.data}

        #use email as username if username is not provided
        if not data.get("username", None):
            data["username"] = data.get("email", None)
            request.data["username"] = data.get("email", None)

        user_serializer = UserSerializer(data=data)
        user_serializer.is_valid()
        errors = self.validate(data)
        if user_serializer.is_valid() and not errors:           
            data.pop("conf_password") 
            User.objects.create_user(data.pop("username"), data.pop("email"), data.pop("password"), **data)
            return super().post(request, *args, **kwargs)

        return Response(status=400, data={**user_serializer.errors, **errors})

class LoginApiView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        #set email as username when username is not provided
        if not request.data.get("username", None):
            request.data["username"] = request.data.get("email", None)
        return super().post(request, *args, **kwargs)