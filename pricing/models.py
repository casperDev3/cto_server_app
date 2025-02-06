from django.db import models


class Calculation(models.Model):
    products = models.JSONField()  #  деталі вибраних продуктів /api/products/
    services = models.JSONField()  #  деталі вибраних послуг /api/services/  all done
    discount_code = models.CharField(max_length=50, blank=True, null=True) #?
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_applied = models.DecimalField(max_digits=10, decimal_places=2) #?
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Calculation #{self.id} - Final Price: {self.final_price}"
