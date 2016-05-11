from django.conf.urls import patterns, include, url, handler404, handler500
from ecomstore import settings
import os

from django.contrib import admin
admin.autodiscover()

handler404 = handler404
handler500 = handler500

urlpatterns = patterns('',
    url(r'^catalog/$', 'preview.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('catalog.urls')),
    url(r'^cart/', include('cart.urls')),
)

def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__).decode('utf-8')).replace('\\', '/'), *x)

if not settings.DEBUG:
  urlpatterns += patterns('',
      (r'^static/(?P<path>.*)$', 'django.views.static.serve',
      { 'document_root' : rel('static') }),
      )