from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

@require_http_methods(["GET", "POST"])
def all_posts(request):
    if request.method == "GET":
        posts = list(Post.objects.all().values())
        return JsonResponse({"data": posts})
    elif request.method == "POST":
        data = json.loads(request.body)['data']
        post = Post.objects.create(title=data['title'], content=data['content'])
        return JsonResponse({"data": post.__str__()})

