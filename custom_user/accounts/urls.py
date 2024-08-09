from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserUpdateDelete.as_view(), name='user-detail'),
    path('categories/', views.CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryUpdateDelete.as_view(), name='category-detail'),
    path('outfits/list/', views.OutfitList.as_view(), name='outfit-list'),
    path('outfits/create/', views.OutfitCreate.as_view(), name='outfit-list'),
    path('outfits/<int:pk>/', views.OutfitUpdateDestroy.as_view(), name='outfit-detail'),
    path('favorites/', views.FavoriteListCreate.as_view(), name='favorite-list'),
    path('favorites/<int:pk>/', views.FavoriteUpdateDelete.as_view(), name='favorite-detail'),
    path('parts/', views.PartListCreate.as_view(), name='part-list-create'),
    path('parts/<int:pk>/', views.PartUpdateDestroy.as_view(), name='part-detail'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('api-token-auth/', views.CustomAuthToken.as_view())
]