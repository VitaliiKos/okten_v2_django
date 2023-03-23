from django.db import models
from django.core import validators as V


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20,
                             validators=[V.MinLengthValidator(2),
                                         V.RegexValidator(r'^[a-zA-Z]{2,50}$', 'min 2 max 50')])
    year = models.IntegerField(default=2000, validators=[V.MinValueValidator(1990), V.MaxValueValidator(2022)])
    price = models.IntegerField(default=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
