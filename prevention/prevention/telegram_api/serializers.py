from rest_framework import serializers
from prevention.prevention.telegram_api.models import UserRequest
class PreventionSerializer(serializers.Serializer):
    fullName = serializers.CharField(max_length=100)
    phoneNumber = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    telegramUser = serializers.CharField(max_length=50, required=False)

class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = ['id', 'user_id', 'message', 'timestamp']