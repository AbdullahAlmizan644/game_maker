# Generated by Django 4.1 on 2022-12-20 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_category_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]