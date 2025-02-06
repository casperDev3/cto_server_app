from rest_framework import serializers
from .models import Calculation


class CalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculation
        fields = [
            'id', 'products', 'services', 'discount_code',
            'total_price', 'discount_applied', 'final_price', 'created_at'
        ]
