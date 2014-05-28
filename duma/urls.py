from django.conf.urls import patterns, include, url

from django.contrib import admin
#import reporting

admin.autodiscover()
#reporting.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'duma.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^report_builder/', include('report_builder.urls'))
    #url(r'^reporting/', include('reporting.urls')),
)

