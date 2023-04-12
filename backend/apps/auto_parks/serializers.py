from rest_framework.serializers import ModelSerializer

from apps.auto_parks.models import AutoParksModel
from apps.cars.serializers import CarSerializer


class AutoParkSerializer(ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParksModel
        fields = ('id', 'name', 'cars', 'user')
        read_only_fields = ('cars', 'user')
