from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.userListCreate, name="user-list"),
    path("users/", views.userListCreate, name="user-create"),
    path("users/<int:pk>", views.userDetail, name="user-detail"),
    path("categories/", views.categoryListCreate, name="category-list"),
    path("outfits/", views.outfitListCreate, name="outfit-list"),
    path("outfits/", views.outfitListCreate, name="outfit-create"),
    path("favorites/", views.favoriteList, name="favorite-list"),

]