from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from .models import Service
from decimal import Decimal

@require_http_methods(["GET", "POST"])
def all_services(request):
    if request.method == "GET":
        services = list(Service.objects.all().values())
        if services:
            return JsonResponse({"data": services})
        else:
            return JsonResponse({"data": "Empty"})
    elif request.method == "POST":
        data = json.loads(request.body)['data']
        service = Service.objects.create(
            name=data['name'],
            description=data['description'],
            price=Decimal(data['price']),
            category=data['category']
        )
        return JsonResponse({"data": service.__str__()})

@require_http_methods(["GET", "DELETE", "PUT"])
def service_detail(request, pk):
    try:
        service = Service.objects.get(pk=pk)
        if request.method == "GET":
            return JsonResponse({"data": service.__str__()})
        elif request.method == "DELETE":
            service.delete()
            return JsonResponse({"data": "Service deleted"})
        elif request.method == "PUT":
            data = json.loads(request.body)['data']
            service.name = data['name']
            service.description = data['description']
            service.price = Decimal(data['price'])
            service.category = data['category']
            service.save()
            return JsonResponse({"data": service.__str__()})
    except Exception as e:
        return JsonResponse({"data": f"{e}"})