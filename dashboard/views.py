from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home.models import Team,Tournament
from django.core.files.storage import FileSystemStorage

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
    messages.success(request, "Logged out successfully!")
    return redirect("/")



def add_teams(request,slug):
    if "user" in request.session:
        messages.success(request, "You already add team")
        return redirect("/")

    else:
        tournament=Tournament.objects.filter(tournament_name=slug).first()
        if request.method=="POST":
            team_name=request.POST.get('team_name')
            team_image=request.FILES['team_image']

            player1_name=request.POST.get('player1_name')
            player1_image=request.FILES['player1_image']

            player2_name=request.POST.get('player2_name')
            player2_image=request.FILES['player2_image']

            player3_name=request.POST.get('player3_name')
            player3_image=request.FILES['player3_image']

            player4_name=request.POST.get('player4_name')
            player4_image=request.FILES['player4_image']

            player5_name=request.POST.get('player5_name')
            player5_image=request.FILES['player5_image']

            player6_name=request.POST.get('player6_name')
            player6_image=request.FILES['player6_image']

            player7_name=request.POST.get('player7_name')
            player7_image=request.FILES['player7_image']


            player8_name=request.POST.get('player8_name')
            player8_image=request.FILES['player8_image']


            player9_name=request.POST.get('player9_name')
            player9_image=request.FILES['player9_image']

            player10_name=request.POST.get('player10_name')
            player10_image=request.FILES['player10_image']

            player11_name=request.POST.get('player11_name')
            player11_image=request.FILES['player11_image']

            fss=FileSystemStorage()

            team_image_file=fss.save(team_image.name, team_image)
            team_image_url=fss.url(team_image_file)

            player1_image_file=fss.save(player1_image.name, player1_image)
            player1_image_url=fss.url(player1_image_file)

            player2_image_file=fss.save(player2_image.name, player2_image)
            player2_image_url=fss.url(player2_image_file)

            player3_image_file=fss.save(player3_image.name, player3_image)
            player3_image_url=fss.url(player3_image_file)

            player4_image_file=fss.save(player4_image.name, player4_image)
            player4_image_url=fss.url(player4_image_file)

            player5_image_file=fss.save(player5_image.name, player5_image)
            player5_image_url=fss.url(player5_image_file)


            player6_image_file=fss.save(player6_image.name, player6_image)
            player6_image_url=fss.url(player6_image_file)


            player7_image_file=fss.save(player7_image.name, player7_image)
            player7_image_url=fss.url(player7_image_file)

            player8_image_file=fss.save(player8_image.name, player8_image)
            player8_image_url=fss.url(player8_image_file)

            player9_image_file=fss.save(player9_image.name, player9_image)
            player9_image_url=fss.url(player9_image_file)

            player10_image_file=fss.save(player10_image.name, player10_image)
            player10_image_url=fss.url(player10_image_file)

            player11_image_file=fss.save(player11_image.name, player11_image)
            player11_image_url=fss.url(player11_image_file)




            team=Team(team_manager=request.user,
            team_name=team_name,
            team_image=team_image_url,
            tournament=tournament,
            player1_name=player1_name,
            player1_image=player1_image_url,
            player2_name=player2_name,
            player2_image=player2_image_url,
            player3_name=player3_name,
            player3_image=player3_image_url,
            player4_name=player4_name,
            player4_image=player4_image_url,
            player5_name=player5_name,
            player5_image=player5_image_url,
            player6_name=player6_name,
            player6_image=player6_image_url,
            player7_name=player7_name,
            player7_image=player7_image_url,
            player8_name=player8_name,
            player8_image=player8_image_url,
            player9_name=player9_name,
            player9_image=player9_image_url,
            player10_name=player10_name,
            player10_image=player10_image_url,
            player11_name=player11_name,
            player11_image=player11_image_url,
            )
            team.save()
            request.session["team_name"]=team_name
            messages.success(request, "Your team add successfully")
            return redirect("/")

        return render(request, "dashboard/add_teams.html",{
            "tournament":tournament,
        })

    



@login_required(login_url=user_login)
def team(request):
    team_details=Team.objects.filter(team_manager=request.user).first()

    return render(request, "dashboard/team.html",{
                "team_details":team_details,

            })