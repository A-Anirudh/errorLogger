# Generated by Django 3.2.3 on 2021-06-02 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0022_remove_log_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.RemoveField(
            model_name='solutions',
            name='user',
        ),
    ]