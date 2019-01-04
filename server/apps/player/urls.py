from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^register/$', register),
    url(r'^login/$', login),
    url(r'^user/(?P<user_id>[1-9][0-9]*)/$', profile)
]