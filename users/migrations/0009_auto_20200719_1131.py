# Generated by Django 3.0.5 on 2020-07-19 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200718_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='profile_pics/default.jpeg', upload_to='profile_pics'),
        ),
    ]
