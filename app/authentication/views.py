from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, UserCreateSerializer

class RegisterView(APIView):
    @extend_schema(request=RegisterSerializer, responses={201: dict, 400: dict, 409: dict}, tags=["Auth"])
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"error": "Validation error", "details": serializer.errors}, 400)

        email = serializer.validated_data["email"]
        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already registered"}, 409)

        user = serializer.save()
        token = str(AccessToken.for_user(user))
        return Response({"token": token, "user": {"id": user.id, "name": user.first_name, "email": user.email}}, 201)

class LoginView(APIView):
    @extend_schema(request=LoginSerializer, responses={200: dict, 400: dict, 401: dict}, tags=["Auth"])
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"error": "Validation error", "details": serializer.errors}, 400)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(username=email, password=password)
        if not user:
            return Response({"error": "Invalid email or password"}, 401)

        token = str(AccessToken.for_user(user))
        return Response({"token": token, "user": {"id": user.id, "name": user.first_name, "email": user.email}})

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(responses={200: UserSerializer, 401: dict}, tags=["Auth"])
    def get(self, request):
        return Response(UserSerializer(request.user).data)
