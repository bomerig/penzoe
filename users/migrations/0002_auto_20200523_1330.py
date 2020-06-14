# Generated by Django 3.0.5 on 2020-05-23 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='background_pic',
            field=models.ImageField(blank=True, upload_to='users/%y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='user',
            name='data_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='users/%y/%m/%d/'),
        ),
    ]
