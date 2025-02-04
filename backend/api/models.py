from django.db import models
from django.contrib.auth.models import User
from api.validators import validate_no_numeric_characters, validate_positive, validate_year

class Car(models.Model):
    class FuelType(models.TextChoices):
        GASOLINE = 'G', 'Gasoline'
        ETHANOL = 'T', 'Ethanol'
        DIESEL = 'D', 'Diesel'
        ELETRIC = 'E', 'Electric'
        HYBRID = 'H', 'Hybrid'

    make = models.CharField(max_length=30, blank=False, validators=[validate_no_numeric_characters], db_index=True, editable=False)
    model = models.CharField(max_length=50, blank=False, db_index=True, editable=False)
    year = models.IntegerField(validators=[validate_year], db_index=True, editable=False)
    color = models.CharField(max_length=20, validators=[validate_no_numeric_characters])
    mileage = models.FloatField(validators=[validate_positive])
    price = models.FloatField(validators=[validate_positive], db_index=True)
    fuel_type = models.CharField(max_length=1, choices=FuelType.choices, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, editable=False)
    rented = models.BooleanField(default=False, db_index=True)
    image = models.ImageField(upload_to='car_images/')

    class Meta:
        indexes = [
            models.Index(fields=['year']),
            models.Index(fields=['price']),
            models.Index(fields=['created_at']),
            models.Index(fields=['make', 'model']),
            models.Index(fields=['model', 'rented']),
            models.Index(fields=['year', 'price']),
            models.Index(fields=['year', 'rented']),
            models.Index(fields=['price', 'rented']),
            models.Index(fields=['make', 'model', 'year']),
            models.Index(fields=['make', 'model', 'price']),
            models.Index(fields=['make', 'model', 'rented']),
            models.Index(fields=['year', 'price', 'rented']),
        ]