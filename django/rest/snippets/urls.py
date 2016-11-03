# -*- coding: utf-8 -*-

from django.conf.urls import url, include
# from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
# from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# urlpatterns = [
#     # url(r'^snippets/$', views.snippet_list),
#     # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
#     url(r'^snippets/$', views.SnippetList.as_view()),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
#     url(r'^users/$', views.UserList.as_view()),
#     url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
#     url((r'^$', views.api_root)),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),
# ]
#
# # Using format suffixes gives us URLs that explicitly refer to a given
# # format, and means our API will be able to handle URLs such as
# # http://example.com/api/items/4.json.
# urlpatterns = format_suffix_patterns(urlpatterns)

# # API endpoints
# urlpatterns = format_suffix_patterns([
#     url(r'^$', views.api_root),
#     url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
#     url(r'^users/$', views.UserList.as_view(), name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
# ])
#
# # Login and logout views for the browsable API
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# ]

# snippet_list = views.SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
# snippet_detail = views.SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })
# snippet_highlight = views.SnippetViewSet.as_view({
#     'get': 'highlight',
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = views.UserViewSet.as_view({
#     'get': 'list',
# })
# user_detail = views.UserViewSet.as_view({
#     'get': 'retrieve',
# })
#
# urlpatterns = format_suffix_patterns([
#     url(r'^$', views.api_root),
#     url(r'^snippets/$', snippet_list, name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
#     url(r'^user/$', user_list, name='user-list'),
#     url(r'^user/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
# ])

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'user', views.UserViewSet)

schema_view = get_schema_view(title='Pastebin API')

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url('^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
