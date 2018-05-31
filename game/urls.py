from django.conf.urls import include, url
from . import views

urlpatterns =  [
        url(r'^save/$', views.save, name='save'),
        url(r'^index.htm/$', views.index, name='index'),
        url(r'^positions.json/$', views.json_response, name='json_response'),
]
