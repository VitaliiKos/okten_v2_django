from rest_framework.serializers import ModelSerializer, RelatedField, ValidationError

from core.dataclasses.auto_park_dataclass import AutoPark

from .models import CarModel, CarPhotoModel


class AutoParkRelatedFieldSerializer(RelatedField):

    def to_representation(self, value: AutoPark):
        return {'id': value.id, 'name': value.name}


class CarPhotoSerializer(ModelSerializer):
    class Meta:
        model = CarPhotoModel
        fields = ('photo',)

    def to_representation(self, instance):
        return instance.photo.url


class CarSerializer(ModelSerializer):
    auto_park = AutoParkRelatedFieldSerializer(read_only=True)
    photos = CarPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year', 'price', 'photos', 'auto_park')
