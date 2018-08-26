from django.urls import include, path
from . import views
from home import views as v
from student.views import *
from django.views.generic.base import TemplateView
urlpatterns = [
    path('', views.details),
    path('marks/', views.marks),
    path('logout',v.logout),
    #path('attend/', views.attend),
    path('attend/', AttendanceListView.as_view()),
    #path('generic/<int:id>/', AttendanceListView.as_view())
    
]