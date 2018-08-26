"""CollegeManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path   
from rest_framework.urlpatterns import format_suffix_patterns
from home.views import LogInView,LogOutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('home/',include('home.urls')),
    path('c',include('rest_framework.urls')),
    path('login/', LogInView.as_view()),
    path('logout/', LogOutView.as_view()),
    path('check/',include('home.api_urls')),
]