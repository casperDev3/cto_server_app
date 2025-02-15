from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
import json
from .serializer import UserProfileSerializer
from .models import UserProfile
from .utils.helpers import Helpers


class UserProfileView(View):
    """
    Получение и обновление профиля пользователя по никнейму.
    """

    def get(self, request, nickName):
        """
        Получение профиля по никнейму.
        """
        user_profile = get_object_or_404(UserProfile, nickName=nickName)
        serializer = UserProfileSerializer(user_profile)
        return Helpers.success_response(serializer.data)

    def patch(self, request, nickName):
        """
        Обновление профиля пользователя по никнейму.
        """
        user_profile = get_object_or_404(UserProfile, nickName=nickName)

        try:
            data = json.loads(request.body)  # Получаем JSON из запроса
            serializer = UserProfileSerializer(user_profile, data=data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Helpers.success_updated(serializer.data)
            else:
                return JsonResponse({
                    "success": False,
                    "errors": serializer.errors
                }, status=400)

        except json.JSONDecodeError:
            return Helpers.internal_server_error("Некорректный JSON", status=400)

        except Exception as e:
            return Helpers.internal_server_error(str(e))
