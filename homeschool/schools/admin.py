from django.contrib import admin

from homeschool.schools.models import School

# from .models import School


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("admin",)
