# Generated by Django 3.1.5 on 2021-01-22 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MeetMe', '0002_skillset_rateing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formDate', models.DateField()),
                ('toDate', models.DateField()),
                ('organization_name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]