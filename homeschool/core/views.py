# from django.shortcuts import render

# Create your views here.

from dateutil.relativedelta import MO, SU, relativedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "core/index.html"


class AppView(LoginRequiredMixin, TemplateView):
    template_name = "core/app.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        self.set_week_boundaries(context)
        context["students"] = list(self.request.user.school.students.all())
        return context

    def set_week_boundaries(self, context):
        today = timezone.now().date()
        monday = today + relativedelta(weekday=MO(-1))
        context["monday"] = monday
        sunday = today + relativedelta(weekday=SU(+1))
        context["sunday"] = sunday
