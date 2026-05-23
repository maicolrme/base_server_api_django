from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "email", "password"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 6}}

    name = serializers.CharField(source="first_name", max_length=255)

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["email"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
        )

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "date_joined"]

    name = serializers.CharField(source="first_name")

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "email"]

    name = serializers.CharField(source="first_name", max_length=255)

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["email"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            password="temporary",
        )
