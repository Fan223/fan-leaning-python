from django.urls import re_path

from app import consumers

websocket_urlpatterns = [
    # urls 路径
    re_path(r'ws/(?P<group>\w+)/$', consumers.ChatConsumer.as_asgi())  # consumers 即 views
]
