from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
import json

from .serializer import ReviewSerializer
from .utils.helpers import Helpers
from .models import Review
from .utils.sorting import Sorting
from .utils.processing import Processing


@require_http_methods(["GET", "POST"])
def all_reviews(request):
    try:
        if request.method == "GET":
            reviews = list(Review.objects.all().values())
            # sorted_data = Sorting.sort_by_date(reviews)
            # print("Sorting by date" , sorted_data)
            processing_data = Processing(data=reviews, params=request.GET)
            formatted_data = processing_data.process_data()
            return Helpers.success_response(formatted_data['data'], warnings=formatted_data['warnings'])

        elif request.method == "POST":
            data = json.loads(request.body)
            if "rating" not in data:
                return JsonResponse({
                    "success": False,
                    "error": "Поле 'rating' обязательно!"
                }, status=400)
            reviews = Review.objects.create(
                author=data["author"],
                text=data["text"],
                rating=data["rating"])
            if data["rating"] > 5:
                data["rating"] = 5
            elif data["rating"] < 0:
                data["rating"] = 1
            # return Helpers.success_created(reviews.__str__())
            return Helpers.success_created(reviews)  # Передаём объект, но обрабатываем его в хелпере
    except KeyError as e:
        return Helpers.internal_server_error(f"This field does not exist in the Rating table: {str(e)}",
                                             status=400)
    except Exception as e:
        return Helpers.internal_server_error(str(e))
    # 0602


@require_http_methods(["PUT", "DELETE"])
def reviews_detail(request, pk):
    reviews = get_object_or_404(Review, pk=pk)
    try:
        if request.method == "PUT":

            try:
                data = json.loads(request.body)  # Для raw JSON
            except json.JSONDecodeError:
                return Helpers.internal_server_error("Некорректный JSON")

                # Проверяем и обновляем через сериализатор
            serializer = ReviewSerializer(reviews, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Helpers.success_updated(reviews)


        elif request.method == "DELETE":
            reviews = get_object_or_404(Review, pk=pk)
            reviews.delete()
            return Helpers.success_deleted(reviews)
    except Exception as e:
        return JsonResponse({"data": None, "meta": {}}, status=500)
