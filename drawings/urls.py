from django.conf import settings
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", view=views.Index.as_view(), name="index"),
    re_path(r'^category/(?P<short_title>[\w-]+)/$', views.DrawingListView.as_view(), name='draws'),
]