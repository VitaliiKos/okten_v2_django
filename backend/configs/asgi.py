"""
ASGI configs for configs project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from core.middlewares.auth_socket_middleware import AuthSocketMiddleWare
from django.core.asgi import get_asgi_application

from .routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthSocketMiddleWare(URLRouter(websocket_urlpatterns))
})
