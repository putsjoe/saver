from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_url, name='get_url'),
    url(r'hello^$', views.index, name='index'),
]
