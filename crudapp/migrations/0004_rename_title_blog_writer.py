# Generated by Django 3.2.5 on 2021-07-03 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_alter_blog_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='title',
            new_name='writer',
        ),
    ]
