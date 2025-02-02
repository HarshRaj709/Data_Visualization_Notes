# Generated by Django 4.2.6 on 2024-07-03 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Username",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Languages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Python", models.IntegerField()),
                ("Java", models.IntegerField()),
                ("Php", models.IntegerField()),
                ("Cotlin", models.IntegerField()),
                ("Golang", models.IntegerField()),
                (
                    "User",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="userlang",
                        to="data.username",
                    ),
                ),
            ],
        ),
    ]
