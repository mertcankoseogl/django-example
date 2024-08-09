from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        return self.create_user(username, email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.CharField(max_length=128)
    gender = models.IntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    register_date = models.DateField(auto_now_add=True)
    biography = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=200, unique=True, null=False, blank=False)
    user_image = models.ImageField(null=True, blank=True, upload_to="images/profile_images")
    
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_staff = models.BooleanField(default=False, null=True, blank=True)
    is_superuser = models.BooleanField(default=False, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        from django.contrib.auth.hashers import make_password
        self.password = make_password(raw_password)
    

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    category_image = models.ImageField(null=True, blank=True, upload_to="images/category_images")

    def __str__(self):
        return self.title


class Outfit(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_outfit')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_outfit')
    outfit_title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True)
    is_favorited = models.BooleanField(null=True, blank=True)
    is_kid = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.outfit_title


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_favorite')
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE, related_name='outfit_favorite')

    class Meta:
        unique_together = ('user', 'outfit')
        
    def __str__(self):
        return f"{self.user.username} -> {self.outfit.outfit_title}"


class Part(models.Model):
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE, related_name='outfit_parts')
    name = models.CharField(max_length=50, null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class OutfitImages(models.Model):
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE, related_name='outfit_images')
    outfit_image = models.ImageField(null=True, blank=True, upload_to="images/outfit_images")

 
class Follower(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed')

    class Meta:
        unique_together = ('follower', 'followed')

    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"
    

