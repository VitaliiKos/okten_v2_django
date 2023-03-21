from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer, GetCarSerializer


class CarListCreateView(APIView):

    @staticmethod
    def get(*args, **kwargs):

        cars = CarModel.objects.all()
        serializer = GetCarSerializer(instance=cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CarUpdateDeleteView(APIView):

    @staticmethod
    def get(*args, **kwargs):
        pk = kwargs.get('pk')
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('Not Found', status=status.HTTP_404_NOT_FOUND)
        serializer = GetCarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data

        try:
            car = CarModel.objects.get(pk=pk)

        except CarModel.DoesNotExist:
            return Response('Not Found', status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car, data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data

        try:
            car = CarModel.objects.get(pk=pk)

        except CarModel.DoesNotExist:
            return Response('Not Found', status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car, data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)

    @staticmethod
    def delete(*args, **kwargs):
        pk = kwargs.get('pk')
        try:
            car = CarModel.objects.get(pk=pk)

        except CarModel.DoesNotExist:
            return Response('Not Found', status.HTTP_404_NOT_FOUND)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
