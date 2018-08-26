from django import forms


class LoginForm(forms.Form):
    id=forms.CharField(label="Username",max_length=10)
    password=forms.CharField(label="password",max_length=15,widget=forms.PasswordInput)
