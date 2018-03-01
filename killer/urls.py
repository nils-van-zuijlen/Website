from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^view/(?P<pk>[0-9]+)$', views.view, name='view'),

    url(r'^admin$', views.admin, name='admin'),
    url(r'^admin/add$', views.add, name='add'),
]

