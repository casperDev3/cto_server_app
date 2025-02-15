from django.http import JsonResponse
import logging

# Создаем логгер для ошибок
logger = logging.getLogger(__name__)


class Helpers:
    @staticmethod
    def success_response(data, status=200, warnings=None):
        """
        Отправка успешного ответа с переданными данными.
        :param data: Данные для ответа.
        :param status: HTTP статус.
        :param warnings: Предупреждения (если есть).
        :return: JsonResponse с данными.
        """
        return JsonResponse({
            "data": data,
            "meta": {},  # Пустой meta для общего ответа
            "success": True,
            "warnings": warnings or [],  # Пустой список предупреждений, если их нет
        }, status=status)

    @staticmethod
    def success_created(data, status=201):
        """
        Отправка ответа при успешном создании ресурса.
        :param data: Сериализованные данные.
        :param status: HTTP статус (по умолчанию 201).
        :return: JsonResponse с созданным ресурсом.
        """
        return JsonResponse({
            "data": data,  # Данные ресурса
            "meta": {"api_version": "1.0"},  # Версия API для отслеживания изменений
            "success": True,
        }, status=status)

    @staticmethod
    def success_updated(data, status=200):
        """
        Отправка ответа при успешном обновлении ресурса.
        :param data: Обновленные данные.
        :param status: HTTP статус (по умолчанию 200).
        :return: JsonResponse с обновленным ресурсом.
        """
        return JsonResponse({
            "data": data,
            "meta": {"api_version": "1.0"},
            "success": True,
        }, status=status)

    @staticmethod
    def success_deleted(status=200):
        """
        Отправка ответа при успешном удалении ресурса.
        :param status: HTTP статус (по умолчанию 200).
        :return: JsonResponse с успешным удалением.
        """
        return JsonResponse({
            "meta": {"message": "Successfully deleted"},
            "success": True,
        }, status=status)

    @staticmethod
    def internal_server_error(error, status=500):
        """
        Отправка ответа об ошибке сервера.
        :param error: Ошибка для логирования и отображения.
        :param status: HTTP статус (по умолчанию 500).
        :return: JsonResponse с ошибкой.
        """

        logger.error(f"Internal Server Error: {error}")

        return JsonResponse({
            "data": None,
            "meta": {"error": str(error)},
            "success": False,
        }, status=status)
