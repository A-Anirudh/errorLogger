# Generated by Django 3.2.3 on 2021-06-12 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_verified',
        ),
    ]
