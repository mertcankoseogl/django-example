from rest_framework import serializers
from .models import User, Favorite, Outfit, Category, Part, OutfitImages

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PartSerializer(serializers.ModelSerializer):
    outfit = serializers.PrimaryKeyRelatedField(queryset=Outfit.objects.all())
    class Meta:
        model = Part
        fields = "__all__" 


class GetPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ['name', 'link'] 


class GetImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitImages
        fields = ['outfit_image'] 


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    outfit = serializers.PrimaryKeyRelatedField(queryset=Outfit.objects.all())
    class Meta:
        model = Favorite
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    user_favorite = FavoriteSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'fullname', 'email', 'gender', 'birthday',
                   'user_image', 'password', 'register_date', 'user_favorite']


class UserForGetOutfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_image']


class GetOutfitSerializer(serializers.ModelSerializer):
    user = UserForGetOutfitSerializer()
    category = CategorySerializer()
    outfit_parts = GetPartSerializer(many=True, read_only=True)
    class Meta:
        model = Outfit
        fields = "__all__"


class CreateOutfitSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    outfit_parts = GetPartSerializer(many=True)
    outfit_images = GetImageSerializer(many=True)

    class Meta:
        model = Outfit
        fields = ['outfit_title', 'description', 'category', 'outfit_parts', 'outfit_images', 'user']

    def create(self, validated_data):
        outfit_parts_data = validated_data.pop('outfit_parts', [])
        outfit_images_data = validated_data.pop('outfit_images', [])
        outfit = Outfit.objects.create(**validated_data)

        # Handle the creation of outfit parts
        for part_data in outfit_parts_data:
            Part.objects.create(outfit=outfit, **part_data)

         # Handle the creation of outfit images
        for image_data in outfit_images_data:
            # Only include `outfit_image` from image_data
            image_file = image_data.get('outfit_image')
            OutfitImages.objects.create(outfit=outfit, outfit_image=image_file)

        return outfit


class UserRegistrationSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'password']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
 