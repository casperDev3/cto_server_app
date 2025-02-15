from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/blog/', include('blog.urls')),
    path('api/v1/services/', include('service.urls')),
    path('api/v1/prevention/', include('prevention.urls')),
]
