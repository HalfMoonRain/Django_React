# Generated by Django 4.2.1 on 2023-05-22 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instagram", "0004_post_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="photo",
            field=models.ImageField(blank=True, upload_to="instagram/post/%Y/%m/%d"),
        ),
    ]
