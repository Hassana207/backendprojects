from django.shortcuts import render,redirect
from .forms import RegisterUser , ComfirmUser
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages

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

def forgot_password(request):
    if request.method == "POST":
        form = ComfirmUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            new_password = form.cleaned_data["new_password"]
            try:
              user = User.objects.get(username=username)
              user.set_password(new_password)
              user.save()
              messages.success(request,"Password reset successfully")
              return redirect("login")
            except User.DoesNotExist:
                messages.error(request,"User can not be found")
    else:
        form = ComfirmUser()
    return render(request,"forgot_password.html",{"form":form})



