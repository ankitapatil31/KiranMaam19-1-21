# Generated by Django 3.1.5 on 2021-01-19 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MeetMe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillset',
            name='Rateing',
            field=models.IntegerField(default=10),
        ),
    ]
