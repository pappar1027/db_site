from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^BP options/$', views.index, name='index'),
    url(r'^BP options/(?P<data_type>\w*)/$', views.index, name='index'),

    
]