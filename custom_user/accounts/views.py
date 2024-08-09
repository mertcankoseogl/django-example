
from django.http import JsonResponse
from rest_framework import generics, status
from .models import User, Outfit, Favorite, Category, Part
from .serializers import UserSerializer, FavoriteSerializer, CategorySerializer, UserRegistrationSerializer
from .serializers import  LoginSerializer, PartSerializer, CreateOutfitSerializer, GetOutfitSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
# Create your views here.

# User views
class UserListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Category views
class CategoryListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Outfit views
class OutfitList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Outfit.objects.all()
    serializer_class = GetOutfitSerializer
    parser_classes = (JSONParser)

class OutfitCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Outfit.objects.all()
    serializer_class = CreateOutfitSerializer
    parser_classes = (JSONParser, FormParser, MultiPartParser)

class OutfitUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Outfit.objects.all()
    serializer_class = CreateOutfitSerializer

# Part views
class PartListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Part.objects.all()
    serializer_class = PartSerializer

class PartUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Part.objects.all()
    serializer_class = PartSerializer


# Favorite views
class FavoriteListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


# Register view
class RegisterUser(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            token = Token.objects.create(user=user)
            return JsonResponse({"success": True, "detail": None, "token": token.key}, status=status.HTTP_201_CREATED)
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
        

class Login(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            
            print(f'Attempting to authenticate user: {username}')  # Debugging statement
            
            user = authenticate(username=username, password=password)
            
            if user is None:
                return Response({"success": False, 'detail': 'Invalid credentials'}, status=401)
            
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        
        return Response(serializer.errors, status=400)
    
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            
            if not username or not password:
                return Response({"success": False, 'detail': 'Username and password are required'}, status=400)
            
            user = authenticate(username=username, password=password)
            
            if user is None:
                return Response({"success": False, 'detail': 'Invalid credentials'}, status=401)
            
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        
        return Response(serializer.errors, status=400)
    

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })   