from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/blog/', include('blog.urls')),
    path('api/v1/reviews/', include('reviews.urls')),
    path('api/v1/forms/contact_us/', include('contact_form.urls')),
    path('api/v1/services/', include('service.urls')),
]
