# Generated by Django 3.0.5 on 2020-07-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("users", "0007_remove_user_n_books_upladed")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="background_pic",
            field=models.ImageField(blank=True, upload_to="users/%y/%m/%d/"),
        ),
        migrations.AddField(
            model_name="user",
            name="profile_pic",
            field=models.ImageField(blank=True, upload_to="users/%y/%m/%d/"),
        ),
    ]
