from django.db.models import QuerySet


class CarManager(QuerySet):
    def get_cars_by_auto_park_id(self, id):
        return self.filter(auto_park_id=id)

