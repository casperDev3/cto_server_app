from django.urls import path
from .views import UserProfileView

urlpatterns = [
    path('<str:nickName>/', UserProfileView.as_view(), name='user-profile'),
]
