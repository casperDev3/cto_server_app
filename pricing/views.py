from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal

#from .models import Product, Service, Calculation  # Припускаємо, що моделі Product та Service існують
from .serializers import CalculationSerializer

#Розрахунок ціни
# class PricingCalculateAPIView(APIView):
#     def post(self, request, format=None):
#         data = request.data
#         total_price = Decimal('0.00')
#
#         # Розрахунок для продуктів
#         for prod in data.get('products', []):
#             try:
#                 product = Product.objects.get(pk=prod['id'])
#                 quantity = prod.get('quantity', 1)
#                 total_price += product.price * quantity
#             except Product.DoesNotExist:
#                 continue
#
#         # Розрахунок для послуг
#         for serv in data.get('services', []):
#             try:
#                 service = Service.objects.get(pk=serv['id'])
#                 service_price = service.price
#                 # Якщо опції передаються, можна змінити ціну (наприклад, опція "premium" додає фіксовану суму)
#                 if 'premium' in serv.get('options', []):
#                     service_price += Decimal('50.00')  # приклад додаткової суми для преміум опції
#                 total_price += service_price
#             except Service.DoesNotExist:
#                 continue
#
#         discount_code = data.get('discount_code')
#         discount_applied = Decimal('0.00')
#         # Приклад: якщо введено промокод "SPRING10", застосовується знижка 10%
#         if discount_code == "SPRING10":
#             discount_applied = total_price * Decimal('0.10')
#         final_price = total_price - discount_applied
#
#         result = {
#             "total_price": float(total_price),
#             "discount_applied": float(discount_applied),
#             "final_price": float(final_price)
#         }
#         return Response(result, status=status.HTTP_200_OK)


# Фіктивні дані для Product та Service
DUMMY_PRODUCTS = {
    1: {"id": 1, "name": "Oil Filter", "price": Decimal("100.00")},
    5: {"id": 5, "name": "Brake Pad", "price": Decimal("250.00")},
}

DUMMY_SERVICES = {
    3: {"id": 3, "name": "Oil Change", "price": Decimal("300.00")},
}

class PricingCalculateAPIView(APIView):
    def post(self, request, format=None):
        data = request.data
        total_price = Decimal('0.00')

        # Розрахунок для продуктів із зашлушками
        for prod in data.get('products', []):
            product_data = DUMMY_PRODUCTS.get(prod['id'])
            if not product_data:
                continue  # якщо продукт не знайдено, пропустити
            quantity = prod.get('quantity', 1)
            total_price += product_data["price"] * quantity

        # Розрахунок для послуг із зашлушками
        for serv in data.get('services', []):
            service_data = DUMMY_SERVICES.get(serv['id'])
            if not service_data:
                continue
            service_price = service_data["price"]
            # Приклад: додатковий збір за опцію "premium"
            if 'premium' in serv.get('options', []):
                service_price += Decimal('50.00')
            total_price += service_price

        discount_code = data.get('discount_code')
        discount_applied = Decimal('0.00')
        if discount_code == "SPRING10":
            discount_applied = total_price * Decimal('0.10')
        final_price = total_price - discount_applied

        result = {
            "total_price": float(total_price),
            "discount_applied": float(discount_applied),
            "final_price": float(final_price)
        }
        return Response(result, status=status.HTTP_200_OK)

# Попередня оцінка
class PricingEstimateAPIView(APIView):
    def get(self, request, format=None):
        product_ids = request.query_params.get('product_ids', '')
        service_ids = request.query_params.get('service_ids', '')

        total_price = Decimal('0.00')

        if product_ids:
            for prod_id in product_ids.split(','):
                try:
                    product = Product.objects.get(pk=int(prod_id))
                    total_price += product.price  # за замовчуванням беремо кількість 1
                except Product.DoesNotExist:
                    continue

        if service_ids:
            for serv_id in service_ids.split(','):
                try:
                    service = Service.objects.get(pk=int(serv_id))
                    total_price += service.price
                except Service.DoesNotExist:
                    continue

        result = {
            "base_price": float(total_price)
        }
        return Response(result, status=status.HTTP_200_OK)

#Збереження розрахунку
class PricingSaveAPIView(APIView):
    def post(self, request, format=None):
        data = request.data
        total_price = Decimal('0.00')

        # Розрахунок для продуктів
        for prod in data.get('products', []):
            try:
                product = Product.objects.get(pk=prod['id'])
                quantity = prod.get('quantity', 1)
                total_price += product.price * quantity
            except Product.DoesNotExist:
                continue

        # Розрахунок для послуг
        for serv in data.get('services', []):
            try:
                service = Service.objects.get(pk=serv['id'])
                service_price = service.price
                if 'premium' in serv.get('options', []):
                    service_price += Decimal('50.00')
                total_price += service_price
            except Service.DoesNotExist:
                continue

        discount_code = data.get('discount_code')
        discount_applied = Decimal('0.00')
        if discount_code == "SPRING10":
            discount_applied = total_price * Decimal('0.10')
        final_price = total_price - discount_applied

        calculation_data = {
            "products": data.get('products', []),
            "services": data.get('services', []),
            "discount_code": discount_code,
            "total_price": total_price,
            "discount_applied": discount_applied,
            "final_price": final_price
        }
        serializer = CalculationSerializer(data=calculation_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
