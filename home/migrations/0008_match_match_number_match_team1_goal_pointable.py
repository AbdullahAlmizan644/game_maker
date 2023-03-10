# Generated by Django 4.1 on 2022-12-20 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_tournament_team_match'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='match_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='team1_goal',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Pointable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win', models.IntegerField()),
                ('loss', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('points', models.IntegerField()),
                ('team_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tournament')),
            ],
        ),
    ]
