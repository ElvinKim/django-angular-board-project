from django.conf.urls  import url
from . import member_api
from . import board_api

urlpatterns = [
    url(r'^member/', member_api.member, name='member_join'),
    url(r'^member$', member_api.member, name='member_login'),
]
