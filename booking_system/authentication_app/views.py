from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
@csrf_exempt
def login_user(request):
    if request.method == "POST":

        

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.success(request, ("There was an error logging in, Try again!"))
            return redirect('/login')
        
    else:
        if request.user.is_anonymous:
            return render(request, "authentication_app/login.html", {})
            
        else:
            messages.success(request, ("You are already logged in!"))
            return redirect('/home')


    

def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/home')
        
        else:
            messages.success(request, ("There was an error, Try again!"))
            return redirect('/sign-up')
    else:
        return render(request, "authentication_app/register.html", {})
    


def logout_user(request):
    logout(request)
    return redirect('login_user')
    