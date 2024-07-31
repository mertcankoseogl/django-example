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
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Outfit
        fields = "__all__"

class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    outfit = serializers.PrimaryKeyRelatedField(queryset=Outfit.objects.all())
    class Meta:
        model = Favorite
        fields = "__all__"