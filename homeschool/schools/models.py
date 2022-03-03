from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from homeschool.core.models import DaysOfWeekModel

# from django.utils.translation import gettext_lazy as _


class School(models.Model):
    """A school to hold students"""

    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text="Administrador de la Escuela",
    )

    class Meta:
        verbose_name = "Escuela"
        verbose_name_plural = "Escuelas"


User = get_user_model()


@receiver(post_save, sender=User)
def create_school(sender, instance, created, **kwargs):
    """A new user gets an associated school."""
    if created:
        School.objects.create(admin=instance)


class SchoolYear(DaysOfWeekModel):

    """A school year to bound start and end dates of the academic year"""

    school = models.ForeignKey(
        "schools.School", on_delete=models.CASCADE, verbose_name="escuela"
    )
    start_date = models.DateField(verbose_name="fecha de inicio")
    end_date = models.DateField(verbose_name="fecha de culminación")

    class Meta:
        verbose_name = "Año Escolar"
        verbose_name_plural = "Años Escolares"


class GradeLevel(models.Model):
    """A student is in a grade level in a given school year"""

    name = models.CharField(verbose_name="nombre", max_length=128)
    school_year = models.ForeignKey(
        "schools.SchoolYear",
        on_delete=models.CASCADE,
        verbose_name="año escolar",
        related_name="grade_levels",
    )

    class Meta:
        verbose_name = "Grado Escolar"
        verbose_name_plural = "Grados Escolares"

    def __str__(self):
        return self.name
