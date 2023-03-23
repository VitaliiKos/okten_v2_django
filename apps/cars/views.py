from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer, GetCarSerializer


class CarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()

    def get_serializer_class(self):
        return CarSerializer if self.request.method != 'GET' else GetCarSerializer


class CarUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()

    def get_serializer_class(self):
        return CarSerializer if self.request.method != 'GET' else GetCarSerializer
