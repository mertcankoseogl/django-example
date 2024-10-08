from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class CustomUser(models.Model):  # Renamed from User to CustomUser
    fullname = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.CharField(max_length=128)
    gender = models.CharField(max_length=10, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    register_date = models.DateField(auto_now_add=True)
    biography = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=200, unique=True, null=False, blank=False)
    user_photo = models.ImageField(null=True, blank=True, upload_to="images/")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  # Add any other required fields here

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False


class Category(models.Model):
    title = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    photo = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title


class Outfit(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='user_o')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True, null=True)
    description = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    photo = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_fav')
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE, related_name='outfit_fav')

    class Meta:
        unique_together = ('user', 'outfit')
        
    def __str__(self):
        return f"{self.user.username} -> {self.outfit.title}"


class Part(models.Model):
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE, related_name='outfit_part')
    name = models.CharField(max_length=50)
    link = models.URLField()
    subtitle = models.TextField()

    def __str__(self):
        return self.name


class Follower(models.Model):
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='followed')

    class Meta:
        unique_together = ('follower', 'followed')

    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"
    