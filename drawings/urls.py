from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from . import views

from .views import Custom404View

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", view=views.Index.as_view(), name="index"),
    re_path(r'^category/(?P<short_title>[\w-]+)/$', views.DrawingListView.as_view(), name='draws'),
    path('<path:path>', Custom404View.as_view(), name='custom_404'),
]
