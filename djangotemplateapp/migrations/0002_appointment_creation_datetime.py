# Generated by Django 5.1.7 on 2025-03-22 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangotemplateapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='creation_datetime',
            field=models.DateTimeField(default='2025-03-22'),
        ),
    ]
