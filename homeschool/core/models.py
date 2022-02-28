from django.db import models
from waffle.models import AbstractUserFlag


class Flag(AbstractUserFlag):
    """Customizable version of Waffle's Flag model."""


class DaysOfWeekModel(models.Model):

    LUNES = 1
    MARTES = 2
    MIERCOLES = 4
    JUEVES = 8
    VIERNES = 16
    SABADO = 32
    DOMINGO = 64

    days_of_week = models.PositiveIntegerField(
        verbose_name="días de la semana",
        help_text="días de la semana en la que hay sesión",
        default=LUNES + MARTES + MIERCOLES + JUEVES + VIERNES,
    )

    class Meta:
        abstract = True

    def runs_on(self, day):
        return bool(self.days_of_week & day)

    @property
    def total_week_days(self):
        total = 0
        for shift_bits in range(7):
            total += (self.days_of_week >> shift_bits) % 2
        return total
