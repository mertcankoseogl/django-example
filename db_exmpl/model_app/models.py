from django.db import models

# Create your models here.

class User(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    user_name = models.CharField(max_length=50, unique=True, null=True)
    password = models.CharField(max_length=128)
    gender = models.CharField(max_length=10, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    register_date = models.DateField(auto_now_add=True)
    biography = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=200, unique=True, null=True)
    user_photo = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.user_name


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
        return f"{self.follower.user_name} follows {self.followed.user_name}"
    

