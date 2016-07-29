from django.conf.urls  import url
from . import views

urlpatterns = [
    url(r'^list/', views.list, name='board_list'),
    url(r'^write/', views.write, name='board_write'),
    url(r'^view/(?P<posting_id>\d+)', views.view, name='board_view'),
    url(r'^edit/(?P<posting_id>\d+)', views.edit, name='board_edit'),
]
