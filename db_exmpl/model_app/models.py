from django.db import models

# Create your models here.

class USER(models.Model):
    Full_Name = models.CharField(max_length = 100)
    User_Name = models.CharField(max_length = 50)
    Password = models.CharField(max_length = 25)
    Gender = models.CharField(max_length = 10)
    Birthday = models.DateField()
    Register_Date = models.DateField()
    Biography = models.TextField()
    Email = models.EmailField()

class CATEGORY(models.Model):
    Catg_Title = models.TextField()
    Gender = models.CharField(max_length = 10)

class OUTFIT(models.Model):
    CategoryId = models.ForeignKey(CATEGORY, on_delete = models.CASCADE)
    User_Id = models.ForeignKey(USER, on_delete = models.CASCADE)
    Title = models.TextField()
    Description = models.TextField()
    Gender = models.CharField(max_length = 10)


class FAVORITE(models.Model):
    User_ID = models.ForeignKey(USER, on_delete = models.CASCADE)
    Outfit_ID = models.ForeignKey(OUTFIT, on_delete = models.CASCADE)

class Part(models.Model):
    Outfit_Id = models.ForeignKey(OUTFIT, on_delete = models.CASCADE)
    Part_Name = models.CharField(50)
    Link = models.CharField(250)
    Subtitle = models.TextField()

class FOLLOWER(models.Model):
    Follower_Id = models.ForeignKey(USER, on_delete = models.CASCADE)
    Followed_Id = models.ForeignKey(USER, on_delete = models.CASCADE)