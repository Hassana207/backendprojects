from django.shortcuts import render,redirect
from .forms import RegisterUser
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def register_user(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user )
            return redirect("login")
    else:
         form = RegisterUser()
    return render (request, "register.html",{"form":form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
             login(request,user)
             if user.is_staff:
                return redirect('adminDashBoard')
             else :
                return redirect("customerDashboard")
             
    else:
            form= AuthenticationForm()
    return render (request,"login.html",{"form":form})
def home(request):
    return render (request,"home.html")


