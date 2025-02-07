import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from team.models import Teammate


@require_http_methods(["GET", "POST"])
def all_teammates(request):
    if request.method == "GET":
        teammates = list(Teammate.objects.all().values())
        return JsonResponse({"data": teammates})
    elif request.method == "POST":
        data = json.loads(request.body)['data']
        teammate = Teammate.objects.create(
            name=data['name'],
            position=data['position'],
            photo=data.get('photo', "https://loremflickr.com/1280/720"),
            age=data.get('age', 0),
            rating=data.get('rating', 0),
            description=data['description']
        )
        return JsonResponse({"data": {"id": teammate.id, "name": teammate.name}})


@require_http_methods(["GET", "DELETE", "PUT"])
def teammate_detail(request, pk):
    try:
        teammate = Teammate.objects.get(pk=pk)
    except Teammate.DoesNotExist:
        return JsonResponse({"error": "Teammate not found"}, status=404)

    if request.method == "GET":
        return JsonResponse({"data": {
            "id": teammate.id,
            "name": teammate.name,
            "position": teammate.position,
            "photo": teammate.photo,
            "age": teammate.age,
            "rating": teammate.rating,
            "description": teammate.description
        }})

    elif request.method == "DELETE":
        teammate.delete()
        return JsonResponse({"data": True})

    elif request.method == "PUT":
        data = json.loads(request.body)['data']
        teammate.name = data['name']
        teammate.position = data['position']
        teammate.photo = data.get('photo', teammate.photo)
        teammate.age = data.get('age', teammate.age)
        teammate.rating = data.get('rating', teammate.rating)
        teammate.description = data['description']
        teammate.save()
        return JsonResponse({"data": {
            "id": teammate.id,
            "name": teammate.name
        }})