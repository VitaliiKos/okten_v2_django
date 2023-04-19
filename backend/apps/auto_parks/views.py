from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import (CreateAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from apps.auto_parks.filters import AutoParkFilter
from apps.auto_parks.models import AutoParksModel
from apps.auto_parks.serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializer
from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filterset_class = AutoParkFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AutoParkCreateListCarsView(CreateAPIView):
    """
    List of auto parks
    """
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


class MyAutoParkView(ListCreateAPIView):
    serializer_class = AutoParkSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        This view should return a list of all the parks
        for the currently authenticated user.
        """
        user = self.request.user
        return AutoParksModel.objects.filter(user_id=user.pk)


class AutoParkUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Get auto park by id
    patch:
        Partial update auto park by id
    put:
        Full update auto park by id
    delete:
        Delete car auto park id
    """
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer
    permission_classes = (IsAuthenticated,)
