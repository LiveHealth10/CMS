from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from .forms import LoginForm
from .models import Student,Course,Parent,Teacher
from django.template import loader
from django.db import connection
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.sessions.models import Session


from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from .serializers import StudentSerializer,LogInSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login , logout as django_logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.sessions.backends.db import SessionStore
class LogInView(APIView):
    
    def post(self,request):
        
        serializer=LogInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validate['user']
        django_login(request,user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token":token.key},status=200)


class LogOutView(APIView):
    authentication_classes=(TokenAuthentication,)
    def post(self,request):
        django_logout(request)
        return Response (status=204)

   


class studentView(viewsets.ModelViewSet):
    queryset= Student.objects.all() 
    serializer_class=StudentSerializer
     
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid:
            id=request.POST.get('id')
            passw=request.POST.get('password')
            auth=request.POST.get('auth')
            model_dic={'Student':Student,'Parent':Parent,'Teacher':Teacher}
            temp=model_dic[auth]
            auth_dic={'Student':['student_id','student_pass'],'Parent':['parent_id','parent_pass'],'Teacher':['teacher_id','teacher_pass']}
            if (id==getattr(temp.objects.get(pk=id),auth_dic[auth][0]) and passw==getattr(temp.objects.get(pk=id),auth_dic[auth][1])):
                
                request.session['stuid']=id
                request.session['auth']=auth
                #request.session['sesid']=s.session_key
                
                return HttpResponseRedirect('./'+auth.lower()+'/')
            else:
                return render(request,'check.html')
    else:
        form=LoginForm()
    
    return render(request,'check.html',{'form':form})

def logout(request):
    request.session.flush()
    return render(request,'logout.html')