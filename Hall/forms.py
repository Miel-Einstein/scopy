from Hall.models import Post,Messages,Videos
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models

class CreationUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email')

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('category',) 

class BlogForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        exclude=('user','slug','likes','dislikes','created_at','upload_to','date')
            
class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('recepteur','file','image')            

class VideoForm(forms.ModelForm):
    class Meta:
        model=Videos
        fields=('category',)  

class VideoAllForm(forms.ModelForm):
    class Meta:
        model=Videos
        fields='__all__'
        exclude=('user',)

        