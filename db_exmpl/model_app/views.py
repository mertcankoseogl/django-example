
from django.http import JsonResponse
from rest_framework import generics, status
from .models import User, Outfit, Favorite, Category
from .serializers import UserSerializer,OutfitSerializer, FavoriteSerializer, CategorySerializer, UserRegistrationSerializer, LoginSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate

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


# Register view
class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            self.perform_create(serializer)
            return JsonResponse({"success": True, "detail": None}, status=status.HTTP_201_CREATED)
        else:
            errors = serializer.errors

            priority_fields = ['email', 'username', 'password']

            detailed_errors = None
            for field in priority_fields:
                if field in errors:
                    detailed_errors = f"{field}: {', '.join(errors[field])}"
                    break

            if detailed_errors is None:
                for field, error in errors.items():
                    if field not in priority_fields:
                        detailed_errors = f"{field}: {', '.join(error)}"
                        break

            return JsonResponse({"success": False, "detail": detailed_errors}, status=status.HTTP_400_BAD_REQUEST)
        

class Login(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
   
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({"success": False,  'detail': 'Invalid credentials'}, status=401)   