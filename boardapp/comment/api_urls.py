from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^$', api.comment_list, name='comment'),
    url(r'^/$', api.comment_list, name='comment'),
]
