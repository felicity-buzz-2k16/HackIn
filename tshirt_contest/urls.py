from django.conf.urls import url
from . import views
urlpatterns = [
		url(r'^$', views.index, name='index'),
		url(r'^notexist/$', views.error, name='error'),
		url(r'^upload/$', views.upload, name='upload'),
		url(r'^design/$', views.detail, name='detail'),
		url(r'^poll/$', views.pollup, name='pollup'),
		url(r'^poll/delete/$', views.polldown, name='polldown'),
    ]