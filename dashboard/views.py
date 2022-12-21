from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):

    if request.user.is_authenticated:
        return redirect("/")

    else:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request, username=username,password=password)
            print(user)

            if user is not None:
                login(request, user)
                messages.success(request,"logged in successfully!")
                return redirect(dashboard)

            else:
                messages.error(request, "Wrong email or password")

        return render(request, "dashboard/login.html")


@login_required(login_url=user_login)
def dashboard(request):
        return render(request, "dashboard/index.html")


def signup(request):
    if request.user.is_authenticated:
        return redirect("/")

    else:
        if request.method=="POST":
            first_name=request.POST["fname"]
            last_name=request.POST["lname"]
            username=request.POST['username']
            email=request.POST["email"]
            password=request.POST["pass1"]
            confirm_password=request.POST["pass2"]

            user=User.objects.filter(username=username).first()


            if user:
                messages.error(request, "Username already exists")

            elif len(username)<4:
                messages.error(request, "Username must be greater than 4 digits")

            elif len(email)<4:
                messages.error(request, "Email must be greater than 4 digits")

            elif len(password)<4:
                messages.error(request, "Password must be greater than 8 digits")

            elif password!=confirm_password:
                messages.error(request, "Password doesn't match ")

            else:
                new_user=User.objects.create_user(username=username,email=email,password=password)
                new_user.first_name=first_name
                new_user.last_name=last_name
                new_user.save()
                messages.success(request, "Account create successfully!")

                return redirect(user_login)


        return render(request, "dashboard/register.html")


def forget_password(request):
    return render(request, "dashboard/password.html")


def user_logout(request):
    logout(request)
    return redirect("/")