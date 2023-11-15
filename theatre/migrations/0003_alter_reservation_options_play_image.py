# Generated by Django 4.2.7 on 2023-11-15 22:56

from django.db import migrations, models
import theatre.models


class Migration(migrations.Migration):
    dependencies = [
        ("theatre", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="reservation",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddField(
            model_name="play",
            name="image",
            field=models.ImageField(
                null=True, upload_to=theatre.models.play_image_file_path
            ),
        ),
    ]
