from pyexpat import model
import factory
from django.conf  import settings

class UserFactory(factory.django.DjanoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

