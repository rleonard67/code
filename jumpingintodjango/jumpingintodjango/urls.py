from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jumpingintodjango.views.home', name='home'),
    # url(r'^jumpingintodjango/', include('jumpingintodjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^questions/$','questionsandanswers.views.index', name='questions'),
    url(r'^questions/(?P<question_id>\d+)/$', 'questionsandanswers.views.question_detail', name='question_detail'),
)
