from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = patterns('',
    url(r'^buzz/portal/admin/', include(admin.site.urls)),
    url(r'^buzz/portal/HackIn/',include('HackIn.urls')),
    url(r'^buzz/portal/accounts/', include('authentication.urls')),
    url(r'^buzz/portal/password_reset/', include('password_reset.urls')),
    url(r'^buzz/portal/tshirt-contest/', include('tshirt_contest.urls')),
    url(r'^buzz/portal/gordian-knot/', include('gordian_knot.urls')),
  ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
