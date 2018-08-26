from django import forms

class StudentIdForm(forms.Form):
    id=forms.CharField(label="Student id",max_length=10)
