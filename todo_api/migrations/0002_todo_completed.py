# Generated by Django 5.0.1 on 2024-01-17 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
