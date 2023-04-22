from apps.auto_parks.routing import websocket_urlpatterns as auto_parks_routing
from channels.routing import URLRouter
from django.urls import path

websocket_urlpatterns = [
    path('api/auto_parks', URLRouter(auto_parks_routing))
]
