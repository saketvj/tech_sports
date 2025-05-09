from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserCreationForm



def login_view(request):

    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username,password) # !!!! Remove this !!!!

        user = authenticate(request,username = username,password= password)
        print(user)
        if user is None:
            context = { "error" : "Username or Password is not correct. Please try again."}
            return render(request,"accounts/login-view.html",context)
        login(request,user)
        return redirect('/posts')
    return render(request,"accounts/login-view.html",context)


def logout_view(request):
    context = {}
    if request.method == "POST":
        logout(request)
        return redirect('/login')
    return render(request,"accounts/logout-view.html",context)

def register_view(request):
    context = {}
    form = CustomUserCreationForm(request.POST or None)
    # print(request.POST  )
    if form.is_valid():
        user = form.save()

        raw_password = form.cleaned_data.get('password1')
        print(raw_password)
        new_user = authenticate(request,username = user.username,password = raw_password)

        if new_user is not None:
            login(request,new_user)
            return redirect('/login')
    context["form"] = form
    return render(request,"accounts/register.html",context)




# Create your views here.
