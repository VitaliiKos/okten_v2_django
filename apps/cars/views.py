from rest_framework import status
from rest_framework.generics import DestroyAPIView, GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel, CarPhotoModel
from apps.cars.serializers import CarPhotoSerializer, CarSerializer


class CarListCreateView(ListAPIView):
    serializer_class = CarSerializer
    filterset_class = CarFilter
    permission_classes = (AllowAny,)

    def get_queryset(self):
        params_dict = self.request.query_params.dict()
        qs = CarModel.objects.all()

        if 'auto_park_id' in params_dict:
            qs = CarModel.objects.get_cars_by_auto_park_id(params_dict['auto_park_id'])

        return qs


class CarUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CarAddPhotosView(GenericAPIView):
    queryset = CarModel.objects.all()

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
    queryset = CarPhotoModel.objects.all()

    def perform_destroy(self, instance):
        instance.photo.delete()
        super().perform_destroy(instance)
