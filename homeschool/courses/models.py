import uuid

from django.db import models

from homeschool.core.models import DaysOfWeekModel

# Create your models here.


class Course(DaysOfWeekModel):
    """A course is a container for tasks in a certain subject area."""

    name = models.CharField(max_length=256, verbose_name="nombre")
    grade_level = models.ForeignKey(
        "schools.GradeLevel", on_delete=models.CASCADE, verbose_name="grado escolar"
    )

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.name


class CourseTask(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True)
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, verbose_name="curso"
    )
    description = models.TextField(verbose_name="descripción")
    duration = models.PositiveIntegerField(
        verbose_name="duración", help_text="Se espera que la duración este en minutos"
    )

    class Meta:
        verbose_name = "Tarea del Curso"
        verbose_name_plural = "Tareas de los Cursos"

    def __str__(self):
        return self.description
