from django.http import JsonResponse

def response_helper(success: bool, message: str = "", status_code: int = 200):
    status_code = 500 if status_code == 200 and success == False else status_code
    return JsonResponse({
        "success": success,
        "message": message
    }, status=status_code)

def telegram_contact_form_message_helper(data):
    message = (
        f"New Contact Us Form Submission:\n\n"
        f"Name: <code>{data.get('name')}</code>\n"
        f"Email: <code>{data.get('email')}</code>\n"
        f"Phone: <code>{data.get('phone')}</code>\n"
        f"Message: <code>{data.get('message')}</code>\n"
    )
    return message