from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    phone=models.IntegerField()
    message=models.TextField(max_length=10000)
    timestamp=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"message from {self.name}"


class Category(models.Model):
    category_name=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.category_name}"


class Blog(models.Model):
    title=models.CharField(max_length=1000)
    slug=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.CharField(max_length=200)
    content=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='static/home/images')
    timestamp=models.DateTimeField()


    def __str__(self):
        return f"{self.title}"





class Comment(models.Model):
    sno=models.AutoField(primary_key=True)
    Comment=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Blog,on_delete=models.CASCADE)
    parents=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.Comment} by {self.user}"





class Tournament(models.Model):
    tournament_name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='static/home/images')
    timestamp=models.DateTimeField()


    def __str__(self):
        return f"{self.tournament_name}"


class Team(models.Model):
    team_name=models.CharField(max_length=255)
    team_image=models.ImageField(upload_to='static/home/images')
    tournament=models.ForeignKey(Tournament,on_delete=models.CASCADE)
    player1_name=models.CharField(max_length=255)
    player1_image=models.ImageField(upload_to='static/home/images')
    player2_name=models.CharField(max_length=255)
    player2_image=models.ImageField(upload_to='static/home/images')
    player3_name=models.CharField(max_length=255)
    player3_image=models.ImageField(upload_to='static/home/images')
    player4_name=models.CharField(max_length=255)
    player4_image=models.ImageField(upload_to='static/home/images')
    player5_name=models.CharField(max_length=255)
    player5_image=models.ImageField(upload_to='static/home/images')
    player6_name=models.CharField(max_length=255)
    player6_image=models.ImageField(upload_to='static/home/images')
    player7_name=models.CharField(max_length=255)
    player7_image=models.ImageField(upload_to='static/home/images')
    player8_name=models.CharField(max_length=255)
    player8_image=models.ImageField(upload_to='static/home/images')
    player9_name=models.CharField(max_length=255)
    player9_image=models.ImageField(upload_to='static/home/images')
    player10_name=models.CharField(max_length=255)
    player10_image=models.ImageField(upload_to='static/home/images')
    player11_name=models.CharField(max_length=255)
    player11_image=models.ImageField(upload_to='static/home/images')


    def __str__(self):
        return f"Team:  {self.team_name}"


class Match(models.Model):
    match_number=models.IntegerField(default=0)
    team1=models.ForeignKey(Team, related_name='team1',on_delete=models.CASCADE)
    team1_goal=models.IntegerField(default=0)
    team2=models.ForeignKey(Team, related_name='team2',on_delete=models.CASCADE)
    team2_goal=models.IntegerField(default=0)
    veneu=models.CharField(max_length=255)
    timestamp=models.DateTimeField()

    def __str__(self):
        return f"Match no {self.match_number}"



class Pointable(models.Model):
    tournament=models.ForeignKey(Tournament,on_delete=models.CASCADE)
    team_name=models.ForeignKey(Team,on_delete=models.CASCADE)
    win=models.IntegerField()
    loss=models.IntegerField()
    draw=models.IntegerField()
    points=models.IntegerField()


    def __str__(self):
        return f"{self.team_name} pointtable win:{self.win}"


class Match_Video(models.Model):
    video_title=models.CharField(max_length=200)
    video_link=models.CharField(max_length=1000)
    match_image=models.ImageField(upload_to='static/home/images')


    def __str__(self):
        return f"{self.video_title}"