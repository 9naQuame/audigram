from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^setup/$', 'social.views.setup'),
)
