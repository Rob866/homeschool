from django.db import models


class Student(models.Model):
    first_name = models.CharField(verbose_name="Nombre(s)", max_length=64)
    last_name = models.CharField(verbose_name="Apellidos", max_length=64)
    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        verbose_name="escuela",
        related_name="students",
    )

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_courses(self, school_year):
        enrollment = Enrollment.objects.filter(
            student=self, grade_level__in=school_year.grade_levels.all()
        ).first()

        if enrollment:
            for grade_level in school_year.grade_levels.all():
                if grade_level.id == enrollment.grade_level_id:
                    return list(grade_level.courses.all())
        return []

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
