from django.shortcuts import render
from django.http import HttpResponse

from .forms import *

# Create your views here.


def home(request):
    form=Ragistration()
    # return render(request,"home.html",{"form":form})
    if request.method=="POST":
        form=Ragistration(request.POST)
        
        if form.is_valid():
            fname=form.cleaned_data["fname"]  #in square bracket form variable is written there
            lname=form.cleaned_data["lname"]
            email=form.cleaned_data["email"]
            contact=form.cleaned_data["contact"]
            user=stu_Ragistration.objects.filter(email=email)
            if user:
                msg="Email already exist"
                form=Ragistration()
                return render(request,'home.html',{'form':form, 'msg':msg})
            else:
                form.save()
                msg="registration successfully"
                form=Ragistration()
                return render(request,'home.html',{'form':form,'msg':msg})

            # print(fname,lname,email,contact)
            # form.save()
            # data={"fname":fname,"lname":lname,"email":email,"contact":contact}
    return render(request,"home.html",{"form":form})

def login(request):
    form=Login()
    if request.method=='POST':
        data=Login(request.POST)
        login_email=data.cleaned_data['email']
        login_contact=data.cleaned_data['contact']
        user=stu_Ragistration.objects.filter(email=login_email)
        if user:
            user=stu_Ragistration.objects.get(email=login_email)
            print(user)
    return render(request,'login.html',{'form':form})

def logindata(request):

    return HttpResponse("done.......")