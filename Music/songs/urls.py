"""Music URL Configuration

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

from django.urls import path,  re_path
from . import views as songs_views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'songs'
urlpatterns = [
    #home /
    path('', songs_views.home, name='home'),

    #profile_detail /@username/
    path('@<str:username>/', songs_views.profile_detail, name='profile_detail'),

    #add new album /@username/add
    path('@<str:username>/add/',songs_views.add_album, name='add_album'),

    #album's detail page /@username/album/album_name
    path('@<str:username>/album/<str:album>/', songs_views.album_detail, name='album_detail'),

    # login the user /login/
    path('login/', LoginView.as_view(template_name='songs/login.html'), name="login"),

    # signUp new user /signup/
    path('signup/', songs_views.signup, name='signup'),

    #delete album /@username/album/album_name/delete
    path('@<str:username>/album/<str:album>/delete/', songs_views.delete_album, name='delete_album'),

    #add songs to the albums
    path('@<str:username>/album/<str:album>/add/', songs_views.add_song, name='add_song'),

    #logout the current user
    path('logout/', LogoutView.as_view(), name='logout'),
]