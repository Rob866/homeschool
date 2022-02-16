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
