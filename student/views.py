from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from home.models import Marks,Subject,Student,Exam
from home.models import Attendance
from rest_framework import generics
from rest_framework import mixins
from student.serializers import AttendanceSerializer,MarksSerializer
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
import json
# Create your views here.
def details(request):
    try:
        if request.session['auth']=='Student' or request.session['auth']=='Parent' :
            return render(request,'welcome.html',{})
        else:
            request.session.flush()
            return HttpResponseRedirect('/home/')
    except KeyError:
        request.session.flush()
        return HttpResponseRedirect('/home/')

def marks(request):
    try:
        sid=request.session['stuid']
        eid=request.POST.get('exam_id')
        sub=Marks.objects.filter(student_id=sid,exam_id=eid).distinct()
        si=[]
        marks=[]
        for a in sub:
            si.append(a.sub_id_id)
            marks.append(a.marks)
        sn=[]
        for x in si:
            sn.append(Subject.objects.get(pk=x).sub_name)
        res=zip(sn,marks)
        dic={}
        for i in res:
            dic[i[0]]=i[1]
        l= len(dic)
        length=False
        if l>0:
            length=True
        return render(request,'marks.html',{'dic':dic,'length':length})
    except KeyError:
        request.session.flush()
        return HttpResponseRedirect('/home/')




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
    permission_classes=[IsAuthenticatedOrReadOnly]
  
       
    def list(self, request):
        try:

            id=request.session['stuid']
            queryset=Attendance.objects.filter(student_id=id).order_by('-date')
            serializer = AttendanceSerializer(queryset, many=True)
            return serializer.data
        except KeyError:
            request.session.flush()
            return HttpResponseRedirect('/home/')

    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            obj=self.list(request)
            lis = []
            for val in obj:
                lis.append(dict(val))
            y=json.dumps(lis)
          
            return render (request,"./attendance.html",{'lis1':y})
    
   
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
    permission_classes=[IsAuthenticated,IsAdminUser]

    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
        
    
    def post(self,request):
        return self.create(request)
    
    def perform_create(self,serializer):
        serializer.save()

    
    def delete(self,request,id=None):
        return self.destroy(request,id)

'''  
























