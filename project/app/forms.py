from django import forms
from .models import stu_Ragistration

class Ragistration(forms.ModelForm):
    # fname=forms.CharField(max_length=50,label="first name")
    # lname=forms.CharField(max_length=20,label="last name")
    # email=forms.EmailField(label="email")
    # contact=forms.IntegerField(label="contact")
    class Meta:
        model=stu_Ragistration
        fields='__all__'


class Login(forms.ModelForm):
    class Meta:
        model=stu_Ragistration
        fields=('email','contact')