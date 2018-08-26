from django.db import models

# Create your models here.

class Course(models.Model):
    course_id=models.CharField(max_length=15,primary_key=True)
    course_name=models.CharField(max_length=20)
    def __str__(self):
        return self.course_id
class Department (models.Model):
    department_id=models.CharField(max_length=20,primary_key=True)
    department_name=models.CharField(max_length=20)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.department_id

class Subject(models.Model):
    sub_id=models.CharField(max_length=10,primary_key=True,)
    sub_name=models.CharField(max_length=20)
    sub_credit=models.CharField(max_length=2)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.sub_id
    
class Exam(models.Model):
    exam_id=models.CharField(max_length=10,primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.exam_id


class Student(models.Model):
    student_id=models.CharField(max_length=15,primary_key=True)
    student_pass=models.CharField(max_length=15)
    student_name=models.CharField(max_length=20)
    student_id_DOB=models.DateField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_enr_year=models.CharField(max_length=4)
    def __str__(self):
        return self.student_id
        

 

class Teacher(models.Model):
    teacher_id=models.CharField(max_length=10,primary_key=True)
    teacher_pass=models.CharField(max_length=20)
    teacher_name=models.CharField(max_length=20)
    teacher_salary=models.CharField(max_length=20)
    sub_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
    department_id=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.teacher_id

class Marks(models.Model):
    class meta:
        unique_together = (('student_id','exam_id','sub_id'),)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    exam_id=models.ForeignKey(Exam,on_delete=models.CASCADE)
    sub_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.CharField(max_length=20)



class Parent(models.Model):
    parent_id=models.CharField(max_length=15,primary_key=True)
    parent_pass=models.CharField(max_length=15)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
        return self.parent_id

class Attendance(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    date=models.DateField()
    status=models.BooleanField()
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
