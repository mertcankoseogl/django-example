from django.shortcuts import render, get_object_or_404

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

# Create your views here.

@api_view(['GET'])
def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
    users = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)   
    