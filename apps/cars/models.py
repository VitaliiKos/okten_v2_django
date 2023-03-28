from django.core import validators as V
from django.db import models

from apps.auto_parks.models import AutoParksModel


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20,
                             validators=[V.MinLengthValidator(2),
                                         V.RegexValidator(r'^[a-zA-Z]{2,50}$', 'min 2 max 50')])
    year = models.IntegerField(validators=[V.MinValueValidator(1990), V.MaxValueValidator(2022)])
    price = models.IntegerField()
    auto_park = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
