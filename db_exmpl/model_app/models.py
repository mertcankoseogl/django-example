from django.db import models

# Create your models here.

class USERS(models.Model):
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

class OUTFITS(models.Model):
    CategoryId = models.ForeignKey(CATEGORY, on_delete = models.CASCADE)
    User_Id = models.ForeignKey(USERS, on_delete = models.CASCADE)
    Title = models.TextField()
    Description = models.TextField()
    Gender = models.CharField(max_length = 10)


class FAVORITES(models.Model):
    User_ID = models.ForeignKey(USERS, on_delete = models.CASCADE)
    Outfit_ID = models.ForeignKey(OUTFITS, on_delete = models.CASCADE)

class Parts(models.Model):
    Outfit_Id = models.ForeignKey(OUTFITS, on_delete = models.CASCADE)
    Part_Name = models.CharField(50)
    Link = models.CharField(250)
    Subtitle = models.TextField()

class FOLLOWER(models.Model):
    Follower_Id = models.ForeignKey(USERS, on_delete = models.CASCADE)
    Followed_Id = models.ForeignKey(USERS, on_delete = models.CASCADE)