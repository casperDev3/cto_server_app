from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_teammates),
    path('<int:pk>/',views.teammate_detail),
]