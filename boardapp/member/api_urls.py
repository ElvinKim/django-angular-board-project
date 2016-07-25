from django.conf.urls import url
from . import api

urlpatterns = [
    url('', api.member, name='member_join'),
    url(r'^$', api.member, name='member_login'),
]
