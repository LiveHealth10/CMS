from django.shortcuts import render, get_object_or_404, redirect
from teacher.serializer import AttendanceSerializer
from rest_framework.views import APIView
from home.models import Attendance
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from home.models import Marks,Subject,Student,Exam
from home.models import Attendance
from rest_framework import generics
from rest_framework import mixins
from student.serializers import AttendanceSerializer,MarksSerializer
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
import json


# Create your views here.
'''
class AttendanceView(APIView):

    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'try.html'

    def get(self,request,format=None):
        student_id='001'
        date='2018-08-02'
        #attendance=Attendance.objects.filter(student_id=student_id,date=date).distinct()
        attendance = get_object_or_404(Attendance,student_id=student_id,date=date)
        serializer = AttendanceSerializer(attendance)
        return Response({"serializer":serializer,"detail":attendance})
        '''
'''
    def update(self,request,format=None):
        isinstance=self.get_object()
        parents = get_object_or_404(Parent,p_id=p_id)
        data = request.data #this line finish work of JSONparser().parse()
        serializer = ParentSerializer(parents,data=data)
        if not serializer.is_valid():
            return Response({"serializer":serializer,"detail":parents})
        serializer.save()
        return redirect('html_files/parent_list.html')
        '''

'''
class UpdateName(generics.UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]
    lookup_field='pk'

    def update(self, request,pk,format=None):
        instance = self.get_object(pk)
        instance.name = request.data.get("status")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


'''
class AttendanceListView(generics.GenericAPIView,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin
                            ):
    serializer_class=AttendanceSerializer
    queryset=Attendance.objects.all()
    lookup_field='id'
    authentication_classes=[TokenAuthentication,SessionAuthentication,BasicAuthentication]
    #permission_classes=[IsAuthenticated,IsAdminUser]
  
       
    def list(self, request):
        queryset = Attendance.objects.all()
        serializer = AttendanceSerializer(queryset, many=True)
        return serializer.data

    def get(self,request,id=None):
        if request.session['auth']=='Teacher':

            if id:
                return self.retrieve(request,id)
            else:
                obj=self.list(request)
                lis = []
                for val in obj:
                    lis.append(dict(val))
                y=json.dumps(lis)
                return render (request,"./try.html",{'obj':lis,'form':AttendanceSerializer(),'json':y})
        else:
            request.session.flush()
            return HttpResponseRedirect('/home/')


    
    def create(self, request):
        serializer = AttendanceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return serializer
    
    def post(self,request):
        if request.session['auth']!='Teacher':
            return HttpResponseRedirect('/home/')
        serializer = self.create(request)
        return render(request,'./try.html',{'form':serializer})
        
        
  
