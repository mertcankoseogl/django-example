from django.db import models

# Create your models here.

class USER(models.Model):
    Full_Name = models.CharField(max_length = 100, null=True, blank=True)
    User_Name = models.CharField(max_length = 50, unique=True)
    Password = models.CharField(max_length = 128)
    Gender = models.CharField(max_length = 10, null=True, blank=True)
    Birthday = models.DateField(null=True, blank=True)
    Register_Date = models.DateField(auto_now_add = True)
    Biography = models.TextField(null=True, blank=True)
    Email = models.EmailField(max_length = 200, unique=True)
    User_Photo = models.ImageField(null=True, blank=True, upload_to = "images/")


class CATEGORY(models.Model):
    Catg_Title = models.CharField(max_length = 50)
    Gender = models.CharField(max_length = 10)
    Catg_Photo = models.ImageField(upload_to = "images/")


class OUTFIT(models.Model):
    Category_Id = models.ForeignKey(CATEGORY, on_delete = models.CASCADE)
    User_Id = models.ForeignKey(USER, on_delete = models.CASCADE)
    Title = models.CharField(null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Gender = models.CharField(max_length = 10)
    Outfit_Photo = models.ImageField(upload_to = "images/")


class FAVORITE(models.Model):
    User_ID = models.ForeignKey(USER, on_delete = models.CASCADE)
    Outfit_ID = models.ForeignKey(OUTFIT, on_delete = models.CASCADE)


class Part(models.Model):
    Outfit_Id = models.ForeignKey(OUTFIT, on_delete = models.CASCADE)
    Part_Name = models.CharField(max_length = 50)
    Link = models.URLField()
    Subtitle = models.TextField(max_length = 250)


class FOLLOWER(models.Model):
    Follows_Id = models.ForeignKey(
        USER, on_delete = models.CASCADE, related_name='following')
    
    Followed_Id = models.ForeignKey(
        USER, on_delete = models.CASCADE, related_name='followed')