from rest_framework import serializers
from .models import Student
from rest_framework import exceptions
from home.forms import LoginForm
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields='__all__' 
      
class LogInSerializer(serializers.Serializer):

    idi = serializers.IntegerField(read_only=True)
    password=serializers.CharField(max_length=20)
    def validate(self,data):
        idi=data.get('idi','')
        passw=data.get('password','')

        if idi and passw:
            user=authenticate(idi=idi,passw=passw)
            if user:
                if user.is_active:
                    data['user']=user
                else:
                    msg='user is deactivacted'
                    raise exceptions(msg)
            else:
                msg="Enter both userId and password"
                raise exceptions(msg)
        else:
            msg="Enter both userId and password"
            raise exceptions(msg) 
 







    