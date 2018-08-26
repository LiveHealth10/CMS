from django.urls import include, path
from . import views
from parent.views import *
urlpatterns = [
    path('', views.check),
   
]