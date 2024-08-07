from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils import timezone

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


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

        return self.create_user(username, email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.CharField(max_length=128)
    gender = models.CharField(max_length=10, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    register_date = models.DateField(auto_now_add=True)
    biography = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=200, unique=True, null=False, blank=False)
    user_photo = models.ImageField(null=True, blank=True, upload_to="images/")

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    

class Category(models.Model):
    title = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    photo = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title


class Outfit(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='user_o')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True, null=True)
    description = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    photo = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_fav')
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE, related_name='outfit_fav')

    class Meta:
        unique_together = ('user', 'outfit')
        
    def __str__(self):
        return f"{self.user.user_name} -> {self.outfit.title}"


class Part(models.Model):
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE, related_name='outfit_part')
    name = models.CharField(max_length=50)
    link = models.URLField()
    subtitle = models.TextField()

    def __str__(self):
        return self.name


class Follower(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')

    class Meta:
        unique_together = ('follower', 'followed')

    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"
    