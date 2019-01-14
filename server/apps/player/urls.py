from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^register/$', register),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^player/(?P<user_id>[1-9][0-9]*)/$', profile)
    url(r'^character/new', new_character)
]