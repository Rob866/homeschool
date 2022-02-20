import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Course(models.Model):
    """A course is a container for tasks in a certain subject area."""

    name = models.CharField(max_length=256)
    grade_level = models.ForeignKey("schools.GradeLevel", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return self.name


class CourseTask(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True)
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        verbose_name = _("Course Task")
        verbose_name_plural = _("Course Tasks")

    def __str__(self):
        return self.name
