from django.urls import path

from .views import CarListCreateView, CarUpdateDeleteView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='car_list_create'),
    path('/<int:pk>', CarUpdateDeleteView.as_view(), name='car_retrieve_update_delete')
]