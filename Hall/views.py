from django.db.models.query_utils import InvalidQuery
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from rest_framework.response import Response
from Hall.forms import CreationUserForm,VideoAllForm, PostForm,BlogForm,MessageForm,VideoForm
from django.contrib.auth import authenticate, login,logout
from Hall.models import Category,Comment, Messages, Picture, Post, Recepteur,Videos
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import *
from django.http import JsonResponse
from rest_framework.views import APIView

@login_required(login_url='login')
def home(request):
    picture=Picture.objects.filter(user=request.user)
    users=User.objects.all()
    categories=Category.objects.all().order_by('-id')[:1]
    posts=Post.objects.filter(status="published").order_by('?')
    myFilter=PostFilter(request.GET, queryset=posts)
    posts=myFilter.qs
    video=Videos.objects.last()   
  
    return render(request,'home.html',context={'picture':picture,'users':users,'categories':categories,'posts':posts,
    'myFilter':myFilter ,'video':video,})


@login_required(login_url='login')
def profile(request,id):
    user=User.objects.get(id=id)
    postcount=Post.objects.filter(user=user).count()
    posts=Post.objects.filter(user=user).filter(status='published').order_by('?')    
    photo=Picture.objects.filter(user=user)
    return render(request,'profile.html',{'user':user,'photo':photo,'posts':posts,'postcount':postcount})
    

def register(request):
        form=CreationUserForm()
        if request.method=='POST':
            form=CreationUserForm(request.POST)
            if form.is_valid():
                 form.save()
            return redirect('login')
    
        return render(request,'register.html',context={'form':form})

def loginPage(request):
    try:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request, username=username,password=password)  
            if user is not None:
                login(request,user)   
                if request.user.is_superuser:
                    return redirect('dashboard')                                                  
                return redirect('home')
            else:
                messages.info(request, 'username Or password incorrect')     
    except Exception as e:
     
        print(e)    
    return render(request,'login.html',context={})    

def logoutUser(request):
    logout(request)
    return redirect('login')

def add_Post(request):
    form=PostForm
    try: 
      if request.method=='POST':
        form=PostForm(request.POST)  
        user=request.user
        title=request.POST.get('title')
        content=request.POST.get('content')
        image=request.FILES['image']
        if form.is_valid():
            category=form.cleaned_data['category']
        post_obj=Post.objects.create(user=user,title=title,content=content,
        image=image , category=category)
        print(post_obj)
        return redirect('home')
    except Exception as e:
      print(e)
    return render(request,'add_post.html',context={'form':form})  

def add_image_profile(request):
  
  return render(request,'image_profile.html',context={ 
})   

def detail_post(request,id):
  post=Post.objects.get(id=id)
  if  request.method=='POST':
      user=request.user
      post=Post.objects.get(id=id)
      text=request.POST['text']
      new_comment=Comment(text=text,user=user,post=post)
      new_comment.save()
      success=text
      return HttpResponse(success)
  return render(request,'detail_post.html',context={'post':post
}) 



def my_posts(request):
    posts=Post.objects.filter(user=request.user)
    return render(request,'my_posts.html',context={'posts':posts})
def your_videos(request):
    videos= Videos.objects.filter(user=request.user)
    return render(request,'your_videos.html',context={'videos':videos})

def update_post(request,id):
    form=BlogForm()
    post_obj=Post.objects.get(id=id)
    if post_obj.user != request.user:
        redirect('/')
    form=BlogForm(instance=post_obj)    
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES,instance=post_obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'update_Post.html',context={'form':form})

def delete_video(request,id):
   video_obj=Videos.objects.get(id=id)
   if video_obj.user== request.user:
      video_obj.delete()    
   return redirect('my-posts')

def base(request):
    return render(request,'base.html',context={})     

def deletePost(request, id):
    post_obj=Post.objects.get(id=id)
    if post_obj.user == request.user:
        post_obj.delete()
    return redirect('my-posts')

def message_add_view(request,user):
    messages=Messages.objects.filter(user=request.user)
    recepteur=Recepteur.objects.all()
    reponses=Messages.objects.filter(recepteur=recepteur)
    photo=Picture.objects.filter(user=request.user)
    form=MessageForm(request.POST or None,request.FILES or None)
    user=request.user
    sujet=request.POST.get('sujet')
    content=request.POST.get('content')
   
    data={}
    if request.is_ajax():
        if form.is_valid():
            form.save()
            file=form.cleaned_data['file']
            image=form.cleaned_data['image']
            messages_data=Messages.objects.create(user=user,sujet=sujet,content=content,
            file=file, image=image
            )
            data['recepteur']=form.cleaned_data.get('recepteur')
            data['status']='ok'
            print(messages_data)
            return JsonResponse(data)

    context ={
            'form': form,
            'photo':photo,
            'messages':messages,
            'reponses':reponses,
        }    
    return render(request,'messages.html',context)

@login_required(login_url='login')
def dashboard(request):
    subscribeds=User.objects.all()
    uses=User.objects.all()
    post=Post.objects.filter(user=uses).all()
    users=User.objects.all().count()
    posts=Post.objects.filter(status="published").count()
    postcount=Post.objects.filter(user=request.user).all()
    postsubs=Post.objects.filter(status="published")
    videos=Videos.objects.all().count()  

    return render(request,'dashboard.html',context={'users':users,'posts':posts,'videos':videos
    ,'subscribeds':subscribeds,'post':post,'uses':uses,'postsubs':postsubs,'postcount':postcount})

def data_api(request):
    labels=["Users", 'Blue', 'Posts', 'Green', 'Videos', 'Orange']
    qs_count=User.objects.all().count()
    post_count=Post.objects.all().count()
    videos_count=Videos.objects.all().count()  
    default_items=[qs_count,23,post_count,24,videos_count,2]
    data={
        "labels":labels,
        "default":default_items,
    }
    return JsonResponse(data)

def upload_video(request):
    form=VideoForm()
    user=request.user
    if request.method == 'POST': 
        form=VideoForm(request.POST,request.FILES)
        title=request.POST.get('title')
        content=request.POST.get('content')
        image=request.FILES['image']
        video=request.FILES['video']
        if form.is_valid():
            category=form.cleaned_data['category']
        post_videos=Videos.objects.create(title=title,user=user,content=content, image=image,video=video,category=category)
        print(post_videos)
        return redirect('get-videos')
    return render(request,'upload.html',context={'form':form,})


def get_videos(request):    
  videos = Videos.objects.all()
  categories=Category.objects.all()[1::]
  context ={
        'videos':videos,
        'categories':categories,
    }    
  return render(request,'my_videos.html',context)

def update_video(request,id):
    form=VideoAllForm()
    video_obj=Videos.objects.get(id=id)
    if video_obj.user != request.user:
        return redirect('my-posts')
    form=VideoAllForm(instance=video_obj)    
    if request.method=='POST':
        form=VideoAllForm(request.POST,request.FILES,instance=video_obj)
        if form.is_valid():
            form.save()
            return redirect('get-videos')
    context ={'form':form}
    return render(request,'update_video.html',context)

def detail_video(request,id):
    video=Videos.objects.get(id=id)   
    context ={
        'video':video,
    }
    return render(request,'detail_video.html',context)
    
def carousel(request):
    
    return render(request,'caroussel.html',)


class ChartData(APIView):

    def get(self, request, format=None):
       usernames =[user.username for user in User.objects.all()]
       return Response(usernames)
     
