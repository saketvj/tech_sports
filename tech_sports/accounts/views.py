from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib.auth import authenticate,login,logout



def login_view(request):

    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password) # !!!! Remove this !!!!

        user = authenticate(request,username = username,password= password)
        print(user)
        if user is None:
            context = { "error" : "Username or Password is not correct. Please try again."}
            return render(request,"accounts/login-view.html",context)
        login(request,user)
        return redirect('/admin')
    return render(request,"accounts/login-view.html",context)


def logout_view(request):
    context = {}
    if request.method == "POST":
        logout(request)
        return redirect('/login')
    return render(request,"accounts/logout-view.html",context)

def register_view(request):
    pass




# Create your views here.
