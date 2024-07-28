from django.db import models

# Create your models here.

class USER(models.Model):
    Full_Name = models.CharField(max_length = 100)
    User_Name = models.CharField(max_length = 50)
    Password = models.CharField(max_length = 128)
    Gender = models.CharField(max_length = 10)
    Birthday = models.DateField()
    Register_Date = models.DateField(auto_now_add = True)
    Biography = models.TextField(max_length = 250)
    Email = models.EmailField(max_length = 200)
    User_Photo = models.ImageField(null=True, blank=True, upload_to = "images/")

class CATEGORY(models.Model):
    Catg_Title = models.CharField(max_length = 50)
    Gender = models.CharField(max_length = 10)

class OUTFIT(models.Model):
    Category_Id = models.ForeignKey(CATEGORY, on_delete = models.CASCADE)
    User_Id = models.ForeignKey(USER, on_delete = models.CASCADE)
    Title = models.TextField()
    Description = models.TextField()
    Gender = models.CharField(max_length = 10)
    Outfit_Photo = models.ImageField(null=True, blank=True, upload_to = "images/")


class FAVORITE(models.Model):
    User_ID = models.ForeignKey(USER, on_delete = models.CASCADE)
    Outfit_ID = models.ForeignKey(OUTFIT, on_delete = models.CASCADE)

class Part(models.Model):
    Outfit_Id = models.ForeignKey(OUTFIT, on_delete = models.CASCADE)
    Part_Name = models.CharField(max_length = 50)
    Link = models.CharField(max_length = 250)
    Subtitle = models.TextField(max_length = 250)

class FOLLOWER(models.Model):
    Follower_Id = models.ForeignKey(USER, on_delete = models.CASCADE)
    Followed_Id = models.ForeignKey(USER, on_delete = models.CASCADE)