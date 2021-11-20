"""Social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Hall.views import home
from Hall import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('base/',views.base,name='base'),
    path('register/',views.register,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('image-profile/',views.loginPage,name='image'),
    path('add-post/',views.add_Post,name='add-post'),
    path('my-posts/',views.my_posts,name='my-posts'),
    path('your-posts/',views.your_videos,name='your-videos'),
    path('update-post/<id>/',views.update_post,name='update-post'),
    path('delete-post/<id>/',views.deletePost,name='delete-post'),    
    path('post-detail/<id>/',views.detail_post,name='post-detail'),
    path('messages/<user>/',views.message_add_view,name='messages'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('api/data/',views.data_api,name='api-data'),
    path('api/chart/data/',views.ChartData.as_view()),
    path('upload_video/',views.upload_video,name='upload-video'),
    path('videos/',views.get_videos,name='get-videos'),
    path('videos-detail/<id>',views.detail_video,name='video-detail'),
    path('profile/<id>',views.profile,name='profile'),
    path('caroussel/',views.carousel,name='caroussel'),
    path('update_video/<id>',views.update_video,name='update-video'),
    path('delete_video/<id>',views.delete_video,name='delete-video'),








]+static(settings.STATIC_URL ,document_root=settings.STATIC_ROOT)
