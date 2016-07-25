from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^$', api.board, name='board'),
    url(r'^/$', api.board, name='board'),
    url(r'^/(?P<id>\d+)', api.board_detail, name='board_detail'),
]
