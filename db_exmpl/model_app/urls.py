from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.userList, name="user-list"),
    path("users/<int:pk>", views.userDetail, name="user-detail"),
    path("outfits/", views.outfitList, name="outfit-list"),
    path("favorites/", views.favoriteList, name="favorite-list"),
]