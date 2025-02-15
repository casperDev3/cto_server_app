from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=20)
    cover_url = models.URLField(blank=True, null=True)  # необезательно
    avatar_url = models.URLField(blank=True, null=True)  # необезательно
    nickName = models.CharField(max_length=255, unique=True)  # уникально
    joined_date = models.DateField(auto_now_add=True)  # Автоматически при создании
    about = models.CharField(max_length=255, blank=True, null=True)  # необезательно

    def __str__(self):
        return self.name

class CarStats(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='car_stats')
    repairs_count = models.IntegerField()
    car_make = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.car_make} - {self.repairs_count} repairs"
