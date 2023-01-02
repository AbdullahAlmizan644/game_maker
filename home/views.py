from django.shortcuts import render,redirect
from .models import Contact,Blog,Category,Comment,Tournament,Match,Team,Pointable,Match_Video
from django.contrib import messages
from dashboard.views import user_login
from django.contrib.auth import login,authenticate

# Create your views here.
def home(request):
    tournament=Tournament.objects.last()
    last_match=Match.objects.last()
    pointable=Pointable.objects.all()
    blog=Blog.objects.all()
    videos=Match_Video.objects.all()

    return render(request, "home/index.html",{
        "tournament":tournament,
        "last_match":last_match,
        "pointable":pointable,
        "blog":blog,
        "videos":videos,
    })


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
    last_match=Match.objects.last()
    matches=Match.objects.all()
    blog=Blog.objects.all()
    videos=Match_Video.objects.all()
    return render(request, "home/matches.html",{
        "matches":matches,
        "last_match":last_match,
        "blog":blog,
        "videos":videos,
    })



def players(request):
    return render(request, "home/players.html")


def single(request,slug):
    categories=Category.objects.all()
    post=Blog.objects.filter(slug=slug).first()
    comment=Comment.objects.filter(post=post)
    return render(request, "home/single.html",{
        "post":post,
        "categories":categories,
        "comment":comment,

    })


def blog(request):
    blog=Blog.objects.all()
    return render(request, "home/blog.html",{
        "blog":blog,
    })



def user_comment(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            comment=request.POST["comment"]
            user=request.user
            postId=request.POST["postSno"]
            post=Blog.objects.filter(id=postId).first()


            new_comment=Comment(Comment=comment,user=user,post=post)
            new_comment.save()

            messages.success(request,"Your comment add successfully!")

        return redirect("/")

    else:
        return redirect(user_login)

