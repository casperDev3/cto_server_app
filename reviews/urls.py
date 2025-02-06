from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_reviews, name='reviews-all'),
    path('<int:pk>/', views.reviews_detail, name='reviews-detail'),
]
