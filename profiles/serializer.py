from rest_framework import serializers
from .models import UserProfile, CarStats

class CarStatsSerializer(serializers.ModelSerializer):
    """Серіалізатор для CarStats (статистика авто)"""
    repairsCount = serializers.IntegerField(source="repairs_count")  # Перейменовуємо для фронту
    carMake = serializers.CharField(source="car_make")  # Перейменовуєм

    class Meta:
        model = CarStats
        fields = ['repairsCount', 'carMake']

class UserProfileSerializer(serializers.ModelSerializer):

    """Серіалізатор для UserProfile (профіль користувача)"""

    coverUrl = serializers.URLField(source="cover_url", required=False)
    avatarUrl = serializers.URLField(source="avatar_url", required=False)
    joinedDate = serializers.DateField(source="joined_date", read_only=True)
    carStats = CarStatsSerializer(source="car_stats", read_only=True)
    nickName = serializers.CharField(read_only=True)
    about = serializers.CharField(read_only=False)

    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'coverUrl', 'avatarUrl', 'nickName', 'joinedDate', 'about', 'carStats']
