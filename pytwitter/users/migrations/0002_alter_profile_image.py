# Generated by Django 4.2.1 on 2023-05-24 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(default="default.jpeg", upload_to="profile_pics"),
        ),
    ]