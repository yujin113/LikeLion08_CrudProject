# Generated by Django 3.2.5 on 2021-07-25 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_rename_blog_like_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
