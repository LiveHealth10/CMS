from django.urls import include, path
from home import views
from django.views.generic.base import TemplateView
#from .views import UpdateName
from teacher.views import AttendanceListView
urlpatterns = [
    path('',AttendanceListView.as_view()),
    path('<int:id>/', AttendanceListView.as_view()),
    path('logout',views.logout),
    #path('<int:pk>/',UpdateName.as_view()),
    #path('che/',AttendanceView.as_view()),
]