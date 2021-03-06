# Generated by Django 3.2.12 on 2022-02-21 06:08

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("name", models.CharField(max_length=256, verbose_name="nombre")),
            ],
            options={
                "verbose_name": "Curso",
                "verbose_name_plural": "Cursos",
            },
        ),
        migrations.CreateModel(
            name="CourseTask",
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
                ("uuid", models.UUIDField(db_index=True, default=uuid.uuid4)),
                ("description", models.TextField(verbose_name="descripción")),
                (
                    "duration",
                    models.PositiveIntegerField(
                        help_text="Se espera que la duración este en minutos",
                        verbose_name="duración",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courses.course",
                        verbose_name="curso",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tarea del Curso",
                "verbose_name_plural": "Tareas de los Cursos",
            },
        ),
    ]
