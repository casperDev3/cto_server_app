from django.urls import path
from .views import (
    PricingCalculateAPIView,
    PricingEstimateAPIView,
    PricingSaveAPIView,
)

urlpatterns = [
    path('calculate/', PricingCalculateAPIView.as_view(), name='pricing-calculate'),
    path('estimate/', PricingEstimateAPIView.as_view(), name='pricing-estimate'),
    path('save/', PricingSaveAPIView.as_view(), name='pricing-save'),
]
