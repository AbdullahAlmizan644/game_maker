from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("contact",views.contact,name="contact"),
    path("blog-post", views.blog, name="blog"),
    path("single/<str:slug>",views.single,name="single"),
    path("matches",views.matches,name="matches"),
    path("players",views.players,name="players"),
]