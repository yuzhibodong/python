# -*- coding: utf-8 -*-

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]

# Using format suffixes gives us URLs that explicitly refer to a given
# format, and means our API will be able to handle URLs such as
# http://example.com/api/items/4.json.
urlpatterns = format_suffix_patterns(urlpatterns)
