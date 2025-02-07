from django.urls import path
from .views import get_user_requests, create_user_request, update_user_request, delete_user_request

urlpatterns = [
    path('user_requests/', get_user_requests, name='get_user_requests'),
    path('user_requests/create/', create_user_request, name='create_user_request'),
    path('requests/<int:pk>/update/', update_user_request, name='update_user_request'),
    path('requests/<int:pk>/delete/', delete_user_request, name='delete_user_request'),
]
