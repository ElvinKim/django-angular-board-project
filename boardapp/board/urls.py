from django.conf.urls  import url
from . import views

urlpatterns = [
    url(r'^list/', views.list, name='member_join'),
    url(r'^write/', views.write, name='member_join'),
    url(r'^view/(?P<posting_id>\d+)', views.view, name='member_join'),
]
