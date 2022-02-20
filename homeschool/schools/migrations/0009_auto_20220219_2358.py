# Generated by Django 3.2.12 on 2022-02-20 06:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schools", "0008_gradelevel_schoolyear"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="gradelevel",
            options={
                "verbose_name": "Grade Level",
                "verbose_name_plural": "Grade Levels",
            },
        ),
        migrations.AlterModelOptions(
            name="schoolyear",
            options={
                "verbose_name": "School Year",
                "verbose_name_plural": "school Years",
            },
        ),
        migrations.AlterField(
            model_name="gradelevel",
            name="school_year",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="schools.schoolyear",
                verbose_name="school year",
            ),
        ),
    ]