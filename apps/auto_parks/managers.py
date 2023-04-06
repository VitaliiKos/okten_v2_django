from django.db.models import QuerySet


class AutoParkManager(QuerySet):
    def auto_parks_with_cars_year_lt(self, year):
        auto_park_list = self.filter(cars__year__lt=year).distinct()
        return auto_park_list
