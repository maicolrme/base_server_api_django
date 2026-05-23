import os
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
import requests
import time
import json
from datetime import datetime

class NotificationSendSerializer(serializers.Serializer):
    token = serializers.CharField(required=False, allow_blank=True)
    title = serializers.CharField(max_length=255)
    body = serializers.CharField(max_length=1000)
    data = serializers.JSONField(required=False, default=dict)

class RegisterTokenSerializer(serializers.Serializer):
    token = serializers.CharField(min_length=1)
    device = serializers.CharField(required=False, allow_null=True)

class SendNotificationView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(request=NotificationSendSerializer, responses={200: dict, 400: dict, 502: dict}, tags=["Notifications"])
    def post(self, request):
        serializer = NotificationSendSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"error": "Validation error", "details": serializer.errors}, 400)

        data = serializer.validated_data
        device_token = data.get("token") or os.getenv("FCM_DEVICE_TOKEN")
        if not device_token:
            return Response({"error": "Device token is required"}, 400)

        try:
            creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
            if creds_path:
                import firebase_admin
                from firebase_admin import credentials, messaging
                if not firebase_admin._apps:
                    cred = credentials.Certificate(creds_path)
                    firebase_admin.initialize_app(cred)

                msg = messaging.Message(
                    token=device_token,
                    notification=messaging.Notification(title=data["title"], body=data["body"]),
                    data=data.get("data") or {},
                )
                result = messaging.send(msg)
                return Response({"success": True, "messageId": result})
            return Response({"error": "FCM not configured"}, 502)
        except Exception as e:
            return Response({"error": str(e) or "FCM request failed"}, 502)

class TestNotificationView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(responses={200: dict}, tags=["Notifications"])
    def post(self, request):
        return Response({"success": True, "message": "Test notification sent"})

class RegisterTokenView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(request=RegisterTokenSerializer, responses={200: dict, 400: dict}, tags=["Notifications"])
    def post(self, request):
        serializer = RegisterTokenSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"error": "Validation error", "details": serializer.errors}, 400)
        return Response({"success": True, "message": "Token registered"})
