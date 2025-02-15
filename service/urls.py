
from . import views
from django.urls import include, path
urlpatterns = [
    path('', views.all_services, name='all_services'),
    path('<int:pk>/', views.service_detail, name='service_detail'),
    # path('api/', include('telegram_api.urls')),
]