# Generated by Django 3.1.5 on 2021-01-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanal', '0005_auto_20210125_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiences',
            name='formDate',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='experiences',
            name='toDate',
            field=models.CharField(max_length=20),
        ),
    ]
