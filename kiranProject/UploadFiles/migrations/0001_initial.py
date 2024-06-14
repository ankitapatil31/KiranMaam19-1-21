# Generated by Django 3.1.5 on 2021-06-08 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationFileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.IntegerField(choices=[(1, 'For Publication'), (1, 'For Meditation')], default=1)),
                ('pdf', models.FileField(upload_to='UploadedFile/')),
            ],
        ),
    ]
