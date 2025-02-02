from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_services, name='all_services'),
    path('<int:pk>/', views.service_detail, name='service_detail'),
]