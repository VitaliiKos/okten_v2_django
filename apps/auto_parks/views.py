from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.auto_parks.models import AutoParksModel
from apps.auto_parks.serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializer


class AutoParkListCreateView(ListCreateAPIView):
    # queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        params_dict = self.request.query_params.dict()
        print(params_dict)
        qs = AutoParksModel.objects.all()

        if 'cars_year' in params_dict:
            qs = AutoParksModel.objects.auto_parks_with_cars_year_lt(params_dict['cars_year'])

        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AutoParkCreateListCarsView(CreateAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(auto_park=auto_park)

    def get(self, *args, **kwargs):
        auto_park = self.get_object()
        serializer = self.serializer_class(auto_park.cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
