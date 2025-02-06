from django.http import JsonResponse

class Helpers:
    @staticmethod
    def success_response(data,status=200, warnings=None):
        return JsonResponse({
            "data": data,
            "meta": {},
            "success": True,
            "warnings": warnings or [],
        }, status=status)

    @staticmethod
    def success_created(data, status=201):
        return JsonResponse({
            "id": data.id,  # Объект модели, у него есть id
            "data": {
                "author": data.author,
                "rating": data.rating,
                "text": data.text,
                "created_at": data.created_at.isoformat(),
                "updated_at": data.updated_at.isoformat()
            },
            "meta": {
                "api_version": "1.0"
            },

            "success": True,
        }, status=status)


    @staticmethod
    def success_updated(data, status=200):
        return JsonResponse({
            "id": data.id, "data": {

                "author": data.author,
                "rating": data.rating,
                "text": data.text,
                "created_at": data.created_at.isoformat(),
                "updated_at": data.updated_at.isoformat()
            },
            "meta": {
                "api_version": "1.0"
            },

            "success": True,
        }, status=status)


    @staticmethod
    def success_deleted(data, status=200):
        return JsonResponse({
            "data": None,
            "meta": {
                "message" : "Successfully deleted",
            },
            "success": True,
        },status=status)


    @staticmethod
    def internal_server_error(error, status=500):
        return JsonResponse({
            "data": None,
            "meta": {},
            "success": False,
            "error": error,
        },status=500)