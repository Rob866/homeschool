from django.contrib import admin
from .models import School



class SchoolAdmin(School):
    list_display = ("admin",)