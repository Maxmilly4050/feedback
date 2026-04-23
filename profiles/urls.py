from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view(), name="create-profile"),
    path("list/", views.ListProfileView.as_view(), name="list-profile"),
]
