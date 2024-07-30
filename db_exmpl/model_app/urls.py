from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.userList, name="user-list"),
    path("users/<int:pk>", views.userDetail, name="user-detail"),
]