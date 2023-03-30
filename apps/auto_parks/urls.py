from django.urls import path

from .views import AutoParkCreateListCarsView, AutoParkListCreateView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_park_list_create'),
    path('/<int:pk>/cars', AutoParkCreateListCarsView.as_view(), name='auto_park_car_list_create')
]
