from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.CharField(max_length=100)
    image=models.ImageField(upload_to='blog',blank=True)
    likes = models.IntegerField(default=0)
    date_time=models.DateTimeField(null=True)
   # likes = models.ManyToManyField(User, related_name='liked_blogs')
    
#class Like(models.Model):
    #dislike = models.IntegerField(default=0)
    #date = models.DateTimeField(auto_now_add=True,null=True)

class Userdetails(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50,null=True)