# Generated by Django 3.2.5 on 2021-07-25 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_blog_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='blog',
            new_name='post',
        ),
    ]
