from django.contrib import admin
from .models import Student, Parent,Course,Subject,Exam,Teacher,Marks,Attendance,Department
# Register your models here.
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Exam)
admin.site.register(Teacher)
admin.site.register(Marks)
admin.site.register(Attendance)
admin.site.register(Department)
