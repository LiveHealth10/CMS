from django.urls import include, path
from django.contrib import admin
from home.views import LogInView,LogOutView
from django.views.generic.base import TemplateView
from . import views
urlpatterns = [
    path('', views.login),
    path('login/', LogInView.as_view()),
    path('student/',include('student.urls')),
    path('parent/',include('parent.urls')),
    path('teacher/',include('teacher.urls')),
    path('logout/',views.logout), 
    


]