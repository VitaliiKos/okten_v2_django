from datetime import datetime

from core.enums.regex_enum import RegEx
from django.core import validators as V
from django.db import models

from apps.auto_parks.models import AutoParksModel


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20,
                             validators=[V.RegexValidator(RegEx.BRAND.pattern, RegEx.BRAND.msg)])
    year = models.IntegerField(validators=[V.MinValueValidator(1990), V.MaxValueValidator(datetime.now().year)])
    price = models.IntegerField(validators=[V.MinValueValidator(0), V.MaxValueValidator(1000000)])
    auto_park = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
