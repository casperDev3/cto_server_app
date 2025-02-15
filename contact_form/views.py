import json
from django.views.decorators.http import require_http_methods
from contact_form.utils.telegram import send_message_async
from contact_form.utils.helpers import response_helper, telegram_contact_form_message_helper
from contact_form.utils.validators import form_validator


@require_http_methods(["POST"])
def contact_us(request):
    data = json.loads(request.body)
    print(form_validator(data))
    if not (valid := form_validator(data)).get("success"):
        return response_helper(**valid)
    message = telegram_contact_form_message_helper(data)
    try:
        send_message_async(message)
    except Exception as e:
        return response_helper(success=False, message=f"Error sending message to telegram: {e}")

    return response_helper(success=True, message="Form successfully submitted")