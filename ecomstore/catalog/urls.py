from django.conf.urls import *

urlpatterns = patterns('catalog.views',
    url(r'^$', 'index', name='catalog_home'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', 'show_category',
        name='catalog_category'),
    url(r'^product/(?P<product_slug>[-\w]+)/$',  'show_product',
        name='catalog_product'),
)