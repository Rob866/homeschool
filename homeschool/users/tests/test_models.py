from homeschool.schools.models import School
from homeschool.schools.tests.factories import SchoolFactory
from homeschool.test import TestCase


class TestUser(TestCase):
    def test_has_school(self):
        user = self.make_user()
        school = SchoolFactory(admin=user)

        self.assertEqual(school.admin, user)

    def test_create_school(self):
        user = self.make_user()

        self.assertEqual(user.school, School.objects.get(admin=user))
