from django.contrib import admin

from homeschool.students.models import Enrollment, Student

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "school", "first_name", "last_name")
    raw_id_fields = ("school",)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    pass
