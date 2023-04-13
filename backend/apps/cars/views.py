from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import (DestroyAPIView, GenericAPIView,
                                     ListAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel, CarPhotoModel
from apps.cars.serializers import CarPhotoSerializer, CarSerializer


class CarListCreateView(ListAPIView):
    """
    List of Cars
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter
    # permission_classes = (AllowAny,)


class CarUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Get car by id
    patch:
        Partial update car by id
    put:
        Full update car by id
    delete:
        Delete car by id
    """
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllowAny,)


class CarAddPhotosView(GenericAPIView):
    """
    Add  photo to car
    """
    serializer_class = CarPhotoSerializer
    queryset = CarModel.objects.all()

    @swagger_auto_schema(responses={status.HTTP_200_OK: ''})
    def post(self, *args, **kwargs):
        files = self.request.FILES
        car = self.get_object()
        for key in files:
            serializer = CarPhotoSerializer(data={'photo': files[key]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarPhotoDeleteView(DestroyAPIView):
    """
    Delete car's photo by car's id
    """
    serializer_class = CarPhotoSerializer
    queryset = CarPhotoModel.objects.all()

    def perform_destroy(self, instance):
        instance.photo.delete()
        super().perform_destroy(instance)
