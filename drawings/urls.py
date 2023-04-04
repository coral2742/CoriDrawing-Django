from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.Index.as_view(), name="index"),
    path("category/<slug:pk>/", view=views.CategoriesView.as_view(), name="categories"),
]