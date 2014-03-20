from django.conf.urls import patterns, include, url
from django.contrib import admin
from moderation.helpers import auto_discover


admin.autodiscover()
auto_discover()


urlpatterns = patterns(
    '',
    url(r'', include('website.urls')),
    url(r'', include('worm_strains.urls')),
    url(r'', include('storage.urls')),
    url(r'', include('protocols.urls')),

    # lines below enable admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
