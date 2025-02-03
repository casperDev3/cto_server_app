from django.views.decorators.http import require_http_methods
import json
from reviews.helpers import Helpers
from .models import Review

@require_http_methods(["GET", "POST"])
def all_reviews(request):
    if request.method == "GET":
        notifications = list(Review.objects.all().values())
        return Helpers.success_response(notifications)

    elif request.method == "POST":
        data = json.loads(request.body)
        notifications = Review.objects.create(title=data["title"],content=data["content"])
        return Helpers.success_response(notifications.__str__())
