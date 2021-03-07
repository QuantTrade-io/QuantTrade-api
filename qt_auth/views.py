from django.contrib.auth import authenticate, get_user_model
from django.db import transaction
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer, RegistrationSerializer


class Register(APIView):
    """
    The API to register a new user
    """

    parser_classes = (
        MultiPartParser,
        FormParser,
    )
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.on_valid_request_data(serializer.validated_data)

    def on_valid_request_data(self, data):
        email = data.get("email")
        password = data.get("password")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        guidelines_accepted = data.get("are_guidelines_accepted")

        User = get_user_model()

        with transaction.atomic():
            new_user = User.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                guidelines_accepted=guidelines_accepted,
            )

        return Response({"email": new_user.username}, status=status.HTTP_201_CREATED)

class Login(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.on_valid_request_data(serializer.validated_data)
    
    def on_valid_request_data(self, data):
        username = data['email']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            raise AuthenticationFailed()
