# Generated by Django 4.1 on 2023-01-01 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_comment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='team2_goal',
            field=models.IntegerField(default=0),
        ),
    ]