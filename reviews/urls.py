from django.urls import path
from . import views

urlpatterns = [
    path('reviews/',views.all_reviews, name='reviews-all'),
    path('reviews/<int:pk>/', views.reviews_detail, name='reviews-detail'),
]
