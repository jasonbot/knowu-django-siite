from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
import django.contrib.admin
import django.contrib.auth

from .views import state_summary

urlpatterns = patterns('',
    url(r'^admin/', include(django.contrib.admin.site.urls)),
    url(r'^$', state_summary.home, name='home'),
    url(r'^accounts/login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^accounts/profile/$', RedirectView.as_view(pattern_name='home')),
)
