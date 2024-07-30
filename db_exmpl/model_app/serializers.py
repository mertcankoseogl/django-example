from rest_framework import serializers
from .models import User, Favorite, Outfit, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class OutfitSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Outfit
        fields = "__all__"

class FavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    outfit = OutfitSerializer()
    class Meta:
        model = Favorite
        fields = "__all__"