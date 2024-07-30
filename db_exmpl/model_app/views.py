from django.shortcuts import render, get_object_or_404

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Outfit, Favorite, Category
from .serializers import UserSerializer, OutfitSerializer, FavoriteSerializer, CategorySerializer

# Create your views here.

#User requests
@api_view(['GET', 'POST'])
def userListCreate(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
    users = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)   


#category request
@api_view(['GET', 'POST'])
def categoryListCreate(request):
    if request.method =='GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
#Outfit request
@api_view(['GET', 'POST'])
def outfitListCreate(request):
    if request.method =='GET':
        outfits = Outfit.objects.all()
        serializer = OutfitSerializer(outfits, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = OutfitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


#Favorite request
@api_view(['GET'])
def favoriteList(request):
    favorites = Favorite.objects.all()
    serializer = FavoriteSerializer(favorites, many=True)
    return Response(serializer.data)