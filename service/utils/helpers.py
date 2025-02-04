import json
from .validators import *

def parse_request_data(request):
    try:
        return json.loads(request.body).get('data', None)
    except json.JSONDecodeError:
        return None

def validate_service_data(data):
    required_fields = ['name', 'description', 'price', 'category']
    for field in required_fields:
        if field not in data:
            raise ValidationError(f"Missing required field: {field}")

    validate_name(data['name'])
    validate_category(data['category'])

    price_str = data.get('price', '').strip()
    if price_str == "":
        raise ValidationError("Price cannot be empty.")

    try:
        price = Decimal(price_str)
    except Exception:
        raise ValidationError("Price must be a valid decimal number.")

    validate_price(price)
    validate_price(price)