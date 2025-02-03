from django.http import JsonResponse

class Helpers:
    @staticmethod
    def success_response(data,status=200):
        return JsonResponse({
            "data": data,
            "meta": {},
            "success": True,
        }, status=status)

    @staticmethod
    def success_created(data,status=201):
        return JsonResponse({
            "data": data,
            "meta": {},
            "success": True,
        }, status=status)

    @staticmethod
    def interal_server_error(error, status=500):
        return JsonResponse({
            "data": None,
            "meta": {},
            "success": False,
            "error": error,
        },status=500)