from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices
from django.db.models.fields.json import DataContains 
from django.utils import dates,timezone




class Category(models.Model):
   title=models.CharField(max_length=225)
   
   def __str__(self):
       return self.title

      


class Picture(models.Model):
    user=models.ForeignKey(User, blank=True,null=True, on_delete=models.CASCADE)
    photo_de_profil=models.ImageField(blank=True, null=True,upload_to="static/img")


class Post(models.Model):
   
   
    Choices=(('published','Published'),('draft','Draft'))

    title=models.CharField(max_length=225)
    content=models.TextField(blank=True , null=True)        
    slug=models.SlugField(max_length=225, null=True, blank=True,unique_for_date='date')
    user=models.ForeignKey(User, blank=True,null=True, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, blank=True,null=True, on_delete=models.CASCADE )
    image=models.ImageField(upload_to="static/img")
    created_at=models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    likes=models.ManyToManyField(User,blank=True, related_name='blog_posts')
    dislikes=models.ManyToManyField(User,blank=True, related_name='dislike_blog_posts')
    status=models.CharField(max_length=50,choices=Choices,default='Published')
    date=models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return self.title    
    # def count_posts_of(user):
    #     return Post.objects.filter(user=user).count() 

class Comment(models.Model):
    user=models.ForeignKey(User,blank=True,null=True, on_delete=models.DO_NOTHING)
    text=models.TextField(null=True,blank=True)
    post=models.ForeignKey(Post,blank=True,null=True, on_delete=models.CASCADE)
    def __str__(self):
       return str(self.user)

class Recepteur(models.Model):
    user=models.ForeignKey(User,blank=True,null=True, on_delete=models.PROTECT)
    def __str__(self):
        return self.user.username
    

class Messages(models.Model):
    file=models.FileField(blank=True, null=True)
    image=models.ImageField(upload_to="static/file",blank=True,null=True)
    user=models.ForeignKey(User, blank=True,null=True, on_delete=models.PROTECT)
    sujet=models.CharField(max_length=225,blank=True,null=True)
    content= models.TextField(max_length=225,blank=True,null=False)
    recepteur=models.ManyToManyField(Recepteur)
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sujet
        
        

class Videos(models.Model):
     user=models.ForeignKey(User, blank=True,null=True, on_delete=models.PROTECT)
     image=models.ImageField(upload_to="static/file",blank=True,null=True)
     category=models.ForeignKey(Category, blank=True,null=True, on_delete=models.CASCADE )
     title=models.CharField(max_length=225,blank=True,null=True)
     content= models.TextField(max_length=1000,blank=True,null=False)
     video=models.FileField(upload_to="static/video",blank=True,null=True,max_length=1000)        
     comment=models.ForeignKey(Comment, blank=True,null=True, on_delete=models.PROTECT)
     def __str__(self):
        return self.title
