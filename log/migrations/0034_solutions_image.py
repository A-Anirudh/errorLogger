# Generated by Django 3.2.3 on 2021-06-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0033_alter_solutions_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutions',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]