from decimal import Decimal
from django.core.exceptions import ValidationError
import re

def validate_name(name):
    if len(name) > 100:
        raise ValidationError('Name must be less than 100 characters')
    if name == "" or name is None:
        raise ValidationError('Name cannot be an empty string')


def validate_category(category):
    if len(category) > 50:
        raise ValidationError('Category must be less than 50 characters')
    if category == "" or category is None:
        raise ValidationError('Category cannot be an empty string')


def validate_price(price):
    if price == Decimal('0.00'):
        raise ValidationError("Price cannot be 0.00.")
    if price < Decimal('0.00'):
        raise ValidationError("Price cannot be negative.")
    if price > Decimal('999999999.99'):
        raise ValidationError("Price cannot be greater than 999999999.")
    if not re.match(r'^\d+\.\d{1,2}$', str(price)) and not str(price).isdigit():
        raise ValidationError("Price must have at most two decimal places.")
