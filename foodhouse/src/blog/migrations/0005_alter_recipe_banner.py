# Generated by Django 4.2.3 on 2023-10-8 01:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_alter_recipe_categories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="banner",
            field=models.ImageField(
                blank=True,
                default="default-recipe.png",
                null=True,
                upload_to="banners/",
            ),
        ),
    ]