from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class School(models.Model):
    """A school to hold students"""

    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text=_("The school administrator"),
    )

    class Meta:
        verbose_name = _("school")
        verbose_name_plural = _("schools")


class SchoolYear(models.Model):
    """A school year to bound start and end dates of the academic year"""

    school = models.ForeignKey(
        "schools.School", on_delete=models.CASCADE, verbose_name=_("school")
    )
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = _("School Year")
        verbose_name_plural = _("school Years")


class GradeLevel(models.Model):
    """A student is in a grade level in a given school year"""

    name = models.CharField(_("name"), max_length=128)
    school_year = models.ForeignKey(
        "schools.SchoolYear", on_delete=models.CASCADE, verbose_name=_("school year")
    )

    class Meta:
        verbose_name = _("Grade Level")
        verbose_name_plural = _("Grade Levels")

    def __str__(self):
        return self.name
