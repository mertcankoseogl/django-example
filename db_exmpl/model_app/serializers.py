from rest_framework import serializers
from .models import CustomUser, Favorite, Outfit, Category

class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    outfit = serializers.PrimaryKeyRelatedField(queryset=Outfit.objects.all())

    class Meta:
        model = Favorite
        fields = "__all__"


class OutfitSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Outfit
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    user_fav = FavoriteSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = "__all__"


class UserRegistrationSerializer(serializers.ModelSerializer): 
    class Meta:
        model = CustomUser
        fields = ['fullname', 'username', 'email', 'password']


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']




       