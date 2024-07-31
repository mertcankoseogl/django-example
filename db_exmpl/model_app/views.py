from django.shortcuts import render, get_object_or_404

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from .models import User, Outfit, Favorite, Category
from .serializers import UserSerializer,OutfitSerializer, FavoriteSerializer, CategorySerializer, UserRegistrationSerializer

# Create your views here.

# User views
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Category views
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Outfit views
class OutfitListCreate(generics.ListCreateAPIView):
    queryset = Outfit.objects.all()
    serializer_class = OutfitSerializer

class OutfitUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outfit.objects.all()
    serializer_class = OutfitSerializer


# Favorite views
class FavoriteListCreate(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            self.perform_create(serializer)
            return JsonResponse({"success": True, "detail": None}, status=status.HTTP_201_CREATED)
        else:
            # Format validation errors into a single string
            errors = serializer.errors
            detailed_errors = " ".join([f"{field}: {', '.join(error)}" for field, error in errors.items()])
            return JsonResponse({"success": False, "detail": detailed_errors}, status=status.HTTP_400_BAD_REQUEST)
    