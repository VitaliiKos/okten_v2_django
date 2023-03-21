from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
    car_brand = models.CharField(max_length=20)
    car_year = models.IntegerField()
    number_of_seats = models.IntegerField()
    car_body_type = models.CharField(max_length=20)
    car_engine = models.FloatField()

    # def __str__(self):
    #     return str(self.__dict__)
