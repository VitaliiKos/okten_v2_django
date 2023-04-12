from django.urls import path

from .views import CarAddPhotosView, CarListCreateView, CarPhotoDeleteView, CarUpdateDeleteView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='car_list_create'),
    path('/<int:pk>', CarUpdateDeleteView.as_view(), name='car_retrieve_update_delete'),
    path('/<int:pk>/photo', CarAddPhotosView.as_view(), name='cars_add_photo'),
    path('/photo/<int:pk>', CarPhotoDeleteView.as_view(), name='cars_photo_delete'),
]
