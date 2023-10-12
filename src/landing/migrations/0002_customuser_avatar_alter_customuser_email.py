# Generated by Django 4.2.3 on 2023-10-11 12:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("landing", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="avatar",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to="avatars/"
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]