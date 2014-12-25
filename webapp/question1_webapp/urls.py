from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
import django.contrib.admin
import django.contrib.auth

from .views import state_summary
from .views import logout_view

urlpatterns = patterns('',
    url(r'^admin/', include(django.contrib.admin.site.urls)),
    url(r'^$', state_summary.index, name='index'),
    url(r'^home/$', state_summary.home, name='home'),
    url(r'^accounts/login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'login.html'},
        name='login'),
    url(r'^accounts/logout/$', logout_view.logout, name='logout'),
    url(r'^accounts/profile/$', RedirectView.as_view(pattern_name='index')),
)
