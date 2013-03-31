from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import sharpspark_ui

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sharpspark.views.home', name='home'),
    # url(r'^sharpspark/', include('sharpspark.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', 'sharpspark_ui.views.index', name='home'),
    url(r'^contact/', 'sharpspark_ui.views.contact', name='contact'),
    url(r'^about/', 'sharpspark_ui.views.about', name='about'),
    url(r'^blog/', 'sharpspark_ui.views.blog', name='blog'),

    # url(r'^blog/search/', include('zinnia.urls.search')),
    # url(r'^blog/sitemap/', include('zinnia.urls.sitemap')),
    # url(r'^blog/trackback/', include('zinnia.urls.trackback')),
    # url(r'^blog/tags/', include('zinnia.urls.tags')),
    # url(r'^blog/feeds/', include('zinnia.urls.feeds')),
    # url(r'^blog/random/', include('zinnia.urls.random')),
    # url(r'^blog/authors/', include('zinnia.urls.authors')),
    # url(r'^blog/categories/', include('zinnia.urls.categories')),
    # url(r'^blog/comments/', include('zinnia.urls.comments')),
    # url(r'^blog/', include('zinnia.urls.entries'), name='blog'),
    # url(r'^blog/', include('zinnia.urls.archives')),
    # url(r'^blog/', include('zinnia.urls.shortlink')),
    # url(r'^blog/', include('zinnia.urls.quick_entry')),
)
