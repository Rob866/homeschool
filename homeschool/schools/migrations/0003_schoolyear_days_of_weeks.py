# Generated by Django 3.2.12 on 2022-02-25 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schools", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="schoolyear",
            name="days_of_weeks",
            field=models.PositiveIntegerField(
                default=127,
                help_text="días de la semana en la que hay sesión",
                verbose_name="días de la semana",
            ),
        ),
    ]