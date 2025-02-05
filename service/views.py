from django.core.exceptions import ValidationError
from django.views.decorators.http import require_http_methods
from .models import Service
from decimal import Decimal
from django.db.models import Q
from .utils.helpers import validate_service_data, parse_request_data
from .utils.response_helpers import success_response, error_response

@require_http_methods(["GET", "POST"])
def all_services(request):
    try:
        if request.method == "GET":
            services = Service.objects.all().values()

            price_min = request.GET.get("price_min")
            price_max = request.GET.get("price_max")
            category = request.GET.get("category")

            filters = Q()
            if price_min:
                try:
                    filters &= Q(price__gte=Decimal(price_min))
                except ValueError:
                    return error_response("Invalid price_min value")
            if price_max:
                try:
                    filters &= Q(price__lte=Decimal(price_max))
                except ValueError:
                    return error_response("Invalid price_max value")
            if category:
                try:
                    filters &= Q(category__icontains=category)
                except ValueError:
                    return error_response("Invalid category")

            services = services.filter(filters)

            return success_response(list(services.values())) if services.exists() else error_response("No services found")

        elif request.method == "POST":
            data = parse_request_data(request)
            if not data:
                return error_response("Invalid JSON data")
            try:
                validate_service_data(data)
                service = Service.objects.create(
                    name=data['name'],
                    description=data['description'],
                    price=Decimal(data['price']),
                    category=data['category']
                )
                return success_response(service.__str__())
            except (ValidationError, ValueError) as e:
                return error_response(data=str(e))

    except Exception as e:
        return error_response(data=str(e))


@require_http_methods(["GET", "DELETE", "PUT"])
def service_detail(request, pk):
    try:
        service = Service.objects.get(pk=pk)

        if request.method == "GET":
            return success_response(service.__str__())
        elif request.method == "DELETE":
            service.delete()
            return success_response("Service deleted")
        elif request.method == "PUT":
            data = parse_request_data(request)
            if not data:
                return error_response("Invalid JSON data")
            try:
                validate_service_data(data)
                service.name = data['name']
                service.description = data['description']
                service.price = Decimal(data.get('price', '0.00'))
                service.category = data['category']
                service.save()
                return success_response(message="Service updated", data=service.__str__())
            except (ValidationError, ValueError, KeyError) as e:
                return error_response(data=str(e))

    except Service.DoesNotExist:
        return error_response("Service not found", status_code=404)
    except Exception as e:
        return error_response(data=str(e))