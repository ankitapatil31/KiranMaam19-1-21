# Generated by Django 3.1.5 on 2021-01-25 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanal', '0003_auto_20210124_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiences',
            name='currently_working',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='skillset',
            name='Rateing',
            field=models.IntegerField(),
        ),
    ]