from django.urls import path
from . import views

urlpatterns=[
    path("user_login",views.user_login,name="user_login"),
    path("signup",views.signup,name="signup"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("add_teams/<str:slug>",views.add_teams,name="add_teams"),
    path("team",views.team,name="team"),
    path("forget_password",views.forget_password,name="forget_password"),
    path('user_logout',views.user_logout,name="user_logout"),

]