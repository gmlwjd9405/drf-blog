from django.conf.urls import url
from django.contrib import admin

from .views import (
  PostCreateAPIView,
  PostListAPIView,
  PostDetailAPIView,
  PostUpdateAPIView,
  PostDeleteAPIView,
)

urlpatterns = [
  url(r'^$', PostListAPIView.as_view(), name='list'),

  url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
  # url(r'^create/$', post_create),

  # url(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name='detail'),
  # url(r'^(?P<abc>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
  url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
  # url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),

  url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
  url(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),
  # #url(r'^posts/$', "<appname>.views.<function_name>"),
]
