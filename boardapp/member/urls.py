from django.conf.urls  import url
from . import views

urlpatterns = [
    url(r'^join', views.join, name='member_join'),
    url(r'^login', views.login, name='member_login'),
    url(r'^logout', views.logout, name='member_logout'),
]