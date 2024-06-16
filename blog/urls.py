"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from blogs import views
from blogs.views.user_views import UserCreateView
from blogs.views.user_views import LoginView
from blogs.views.posts_views import PostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserCreateView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path("posts/<uuid:pk>/", PostView.as_view(), name="posts"),
    path("posts/", PostView.as_view(), name="posts"),
]
