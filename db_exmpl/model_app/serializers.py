from rest_framework import serializers
from .models import User, Favorite, Outfit


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class OutfitSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Outfit
        fields = "__all__"

class FavoriteSerializer(serializers.ModelSerializer):
    outfit = OutfitSerializer()
    class Meta:
        model = Favorite
        fields = "__all__"