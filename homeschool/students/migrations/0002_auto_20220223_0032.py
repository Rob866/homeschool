# Generated by Django 3.2.12 on 2022-02-23 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schools", "0002_initial"),
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="student",
            options={
                "verbose_name": "Estudiante",
                "verbose_name_plural": "Estudiantes",
            },
        ),
        migrations.AlterField(
            model_name="student",
            name="school",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="schools.school",
                verbose_name="escuela",
            ),
        ),
        migrations.CreateModel(
            name="Enrollment",
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
                (
                    "grade_level",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schools.gradelevel",
                        verbose_name="grado escolar",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="students.student",
                        verbose_name="estudiante",
                    ),
                ),
            ],
        ),
    ]
