from django.shortcuts import render
from .models import Contact,Blog,Category
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "home/index.html")


def contact(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        message=request.POST["message"]


        if len(name)<3 or len(email)<3 or len(phone)<11 or len(message)<10:
            messages.error(request, "Please fill the from correctly")

        else:
            contact=Contact.objects.create(name=name,email=email,phone=phone,message=message)
            contact.save()
            messages.success(request, "Thanks for your message. we will reply you soon")

    return render(request, "home/contact.html")



def matches(request):
    return render(request, "home/matches.html")



def players(request):
    return render(request, "home/players.html")


def single(request,slug):
    categories=Category.objects.all()
    post=Blog.objects.filter(slug=slug).first()
    return render(request, "home/single.html",{
        "post":post,
        "categories":categories,
    })


def blog(request):
    blog=Blog.objects.all()
    return render(request, "home/blog.html",{
        "blog":blog,
    })


