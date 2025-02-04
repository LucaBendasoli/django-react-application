import re
from datetime import date
from django.core.exceptions import ValidationError

def validate_no_numeric_characters(value):
    if re.search(r'\d', value):
        raise ValidationError("The make can't contain numbers.")

def validate_year(value):
	current_year = date.today().year
	if value < 1886 or value > current_year:
		raise ValidationError(f"The year must be between 1886 and {current_year}")

def validate_positive(value):
    if value < 0:
        raise ValidationError("The value must be positive.")