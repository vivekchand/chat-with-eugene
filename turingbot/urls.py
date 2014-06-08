from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'turingbot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'turingbot.views.index', name='index'),
    url(r'^ask/', 'turingbot.views.ask', name='ask'),
    url(r'^admin/', include(admin.site.urls)),
)
