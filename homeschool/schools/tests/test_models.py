from homeschool.schools.tests.factories import SchoolFactory
from homeschool.test import TestCase


class TestSchool(TestCase):
    def test_school_has_admin(self):
        """A school has an administrator."""
        user = self.make_user()
        school = SchoolFactory(admin=user)
        self.assertEqual(school.admin, user)
