from django.urls import path

from .views import (AutoParkCreateListCarsView, AutoParkListCreateView,
                    AutoParkUpdateDeleteView, MyAutoParkView)

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_park_list_create'),
    path('/<int:pk>', AutoParkUpdateDeleteView.as_view(), name='auto_park_retrieve_update_delete'),
    path('/my', MyAutoParkView.as_view(), name='my_auto_park'),
    path('/<int:pk>/cars', AutoParkCreateListCarsView.as_view(), name='auto_park_car_list_create')
]
