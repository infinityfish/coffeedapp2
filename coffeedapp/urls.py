from django.conf.urls import patterns, include, url
from django.conf import settings
# from django.conf.urls.static import static
from django.views.static import serve
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coffeedapp.views.home', name='home'),
    # url(r'^coffeedapp/', include('coffeedapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'', include('core.urls')),
    url(r'^uploads/(?P<path>.*)$', serve, {
    'document_root': settings.MEDIA_ROOT,
    }),
) 