from django.db import models


class Student(models.Model):
    first_name = models.CharField(verbose_name="Nombre(s)", max_length=64)
    last_name = models.CharField(verbose_name="Apellidos", max_length=64)
    school = models.ForeignKey(
        "schools.School", on_delete=models.CASCADE, verbose_name="escuela"
    )

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Enrollment(models.Model):
    """The association between a student and grade level"""

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="estudiante"
    )
    grade_level = models.ForeignKey(
        "schools.GradeLevel", on_delete=models.CASCADE, verbose_name="grado escolar"
    )

    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"


class Coursework(models.Model):

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="estudiante"
    )
    course_task = models.ForeignKey(
        "courses.CourseTask", on_delete=models.CASCADE, verbose_name="tarea del curso"
    )
    complete_date = models.DateField(verbose_name="fecha de finalización")

    class Meta:
        verbose_name = "Trabajo finalizado"
        verbose_name_plural = "Trabajos finalizados"
