from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from app.authentication.serializers import UserSerializer, UserCreateSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema

@extend_schema_view(
    list=extend_schema(tags=["Users"], summary="List users"),
    retrieve=extend_schema(tags=["Users"], summary="Get user"),
    create=extend_schema(tags=["Users"], summary="Create user"),
    update=extend_schema(tags=["Users"], summary="Update user"),
    destroy=extend_schema(tags=["Users"], summary="Delete user"),
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        return UserSerializer
