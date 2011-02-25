from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': 'homepage.html'}),

    (r'^admin/', include(admin.site.urls)),
    (r'^receipt/(?P<id>\d+)/?$', 'auction.views.receipt'),
)
