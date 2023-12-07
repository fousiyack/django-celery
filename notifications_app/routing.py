from django.urls import re_path

from . import consumers
# (?P<room_name>\w+)
websocket_urlpatterns = [
    re_path(r'ws/notification/broadcast/$', consumers.NotificationConsumer.as_asgi()),
]