from rest_framework import serializers
from home.models import Marks,Attendance
class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields='__all__' 

class  AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields='__all__'