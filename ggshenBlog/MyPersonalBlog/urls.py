"""MyPersonalBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from blog import views as blog_views  # new
import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyPersonalBlog.settings')
django.setup()


urlpatterns = [
    path("login/", blog_views.user_login, name="login"),
    path("auth_view/", blog_views.auth_view, name="auth_view"),
    path("logout/", blog_views.logout_view, name="logout"),
    path("index/", blog_views.index, name="index"),
    path("about/", blog_views.about, name="about"),
    path("infopic/", blog_views.infopic, name="infopic"),
    path("list/", blog_views.list, name="list"),
    path("share/", blog_views.share, name="share"),
    path("time/", blog_views.time, name="time"),
    path("search/", blog_views.search, name="search"),
    path('admin/', admin.site.urls),

]