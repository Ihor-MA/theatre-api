# Generated by Django 4.2.7 on 2023-11-16 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("theatre", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="play",
            name="actors",
            field=models.ManyToManyField(related_name="plays", to="theatre.actor"),
        ),
        migrations.AddField(
            model_name="play",
            name="genres",
            field=models.ManyToManyField(related_name="plays", to="theatre.genre"),
        ),
        migrations.AddField(
            model_name="performance",
            name="play",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="performances",
                to="theatre.play",
            ),
        ),
        migrations.AddField(
            model_name="performance",
            name="theatre_hall",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="performances",
                to="theatre.theatrehall",
            ),
        ),
    ]
