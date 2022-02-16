from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _


class Command(BaseCommand):
    help = _("Ingest CSV data from Homeschool Skedtrack")

    def handle(self, *args, **kwargs):
        self.stdout.write("Read in CSV data")
