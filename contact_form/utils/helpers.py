from django.http import JsonResponse

def response_helper(success: bool, message: str = ""):
    return JsonResponse({
        "success": success,
        "message": message
    }, status=200 if success else 500)

def telegram_contact_form_message_helper(data):
    message = (
        f"New Contact Us Form Submission:\n\n"
        f"Name: <code>{data.get('name')}</code>\n"
        f"Email: <code>{data.get('email')}</code>\n"
        f"Phone: <code>{data.get('phone')}</code>\n"
        f"Message: <code>{data.get('message')}</code>\n"
    )
    return message