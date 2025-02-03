from django.urls import path
from . import views

urlpatterns = [
    path('reviews/',views.all_reviews, name='reviews-list-create'),
]
