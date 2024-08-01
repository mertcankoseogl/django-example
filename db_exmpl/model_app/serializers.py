from rest_framework import serializers
from .models import User, Favorite, Outfit, Category


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    outfit = serializers.PrimaryKeyRelatedField(queryset=Outfit.objects.all())

    class Meta:
        model = Favorite
        fields = "__all__"


class OutfitSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
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
        model = User
        fields = "__all__"


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'user_name', 'email', 'password')

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already exist.")
        return value
    
    def validate_user_name(self, value):
        if User.objects.filter(user_name=value).exists():
            raise serializers.ValidationError("This user name is already exist.")
        return value
       