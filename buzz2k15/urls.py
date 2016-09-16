from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^buzz/hackin/admin/', include(admin.site.urls)),
    url(r'^buzz/hackin/',include('hackin.urls')),
    url(r'^buzz/hackin/accounts/', include('authentication.urls')),
    #url(r'^buzz/hackin/password_reset/', include('password_reset.urls')),
  #  url(r'^buzz/portal/tshirt-contest/', include('tshirt_contest.urls')),
  #  url(r'^buzz/portal/gordian-knot/', include('gordian_knot.urls')),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
