from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^/?$', views.index, name='index'),
    url(r'^admin/?$', views.admin_index, name='admin_index'),
    url(r'^admin/manage/?$', views.admin_manage_pizzas, name='admin_manage'),
    url(r'^admin/commands/?$', views.admin_manage_commands, name='admin_command'),
]

