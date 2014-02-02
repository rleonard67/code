from django.conf.urls import patterns, url
from proviver_payee import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^provider_payee/(?<category_name_url>\w+)/$', views.category, name='category'),
)
