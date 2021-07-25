# Generated by Django 3.2.5 on 2021-07-25 08:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='post', through='crudapp.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]