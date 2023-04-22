from channels.routing import URLRouter
from django.urls import path

from .consumers import AutoParkConsumer

websocket_urlpatterns = [
    path('<str:room>', AutoParkConsumer.as_asgi())
]
