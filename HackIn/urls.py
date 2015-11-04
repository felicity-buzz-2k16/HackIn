from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$',views.index, name = 'index'),
    url(r'^contest', views.contest),
    url(r'^sendpassword', views.sendpassword),

    url(r'^ques1/$', views.ques1),
    url(r'^ques2/$', views.ques2),
    url(r'^ques3/$', views.ques3),
    url(r'^ques4/$', views.ques4),
    url(r'^ques5/$', views.ques5),
    url(r'^ques6/$', views.ques6),
    url(r'^ques7/$', views.ques7),
    url(r'^ques8/$', views.ques8),
    url(r'^ques9/$', views.ques9),
    url(r'^ques10/$', views.ques10),
    url(r'^ques11/$', views.ques11),
    url(r'^ques12/$', views.ques12),
    url(r'^ques13/$', views.ques13),
    url(r'^ques14/$', views.ques14),
    url(r'^ques15/$', views.ques15),
]
