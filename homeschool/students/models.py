from django.db import models


class Student(models.Model):
    first_name = models.CharField(verbose_name="Nombre(s)", max_length=64)
    last_name = models.CharField(verbose_name="Apellidos", max_length=64)
    school = models.ForeignKey("schools.School", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
