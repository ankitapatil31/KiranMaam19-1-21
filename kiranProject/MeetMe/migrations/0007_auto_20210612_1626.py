# Generated by Django 3.1.5 on 2021-06-12 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MeetMe', '0006_auto_20210612_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultydevelopment',
            name='Duration',
            field=models.CharField(max_length=50),
        ),
    ]
