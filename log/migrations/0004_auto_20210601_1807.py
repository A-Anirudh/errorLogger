# Generated by Django 3.2.3 on 2021-06-01 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_auto_20210601_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='solution',
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.log')),
            ],
        ),
    ]
