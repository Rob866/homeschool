from homeschool.courses.tests.factories import CourseFactory, CourseTaskFactory
from homeschool.schools.tests.factories import GradeLevelFactory, SchoolFactory
from homeschool.students.tests.factories import (
    CourseworkFactory,
    EnrollmentFactory,
    StudentFactory,
)
from homeschool.test import TestCase


class TestStudent(TestCase):
    def test_factory(self):
        student = StudentFactory()
        self.assertIsNotNone(student)
        self.assertNotEqual(student.first_name, "")
        self.assertNotEqual(student.last_name, "")

    def test_has_school(self):
        school = SchoolFactory()
        student = StudentFactory(school=school)
        self.assertEqual(student.school, school)

    def test_has_first_name(self):
        first_name = "Garcia"
        student = StudentFactory(first_name=first_name)
        self.assertEqual(student.first_name, first_name)

    def test_has_last_name(self):
        last_name = "Perez"
        student = StudentFactory(last_name=last_name)
        self.assertEqual(student.last_name, last_name)

    def test_has_full_name(self):
        student = StudentFactory()
        self.assertEqual(student.full_name, f"{student.first_name} {student.last_name}")

    def test_get_courses(self):
        enrollment = EnrollmentFactory()
        student = enrollment.student
        grade_level = enrollment.grade_level
        course = CourseFactory(grade_level=grade_level)

        courses = student.get_courses(grade_level.school_year)
        self.assertEqual(list(courses), [course])

    def test_str(self):
        student = StudentFactory()
        self.assertEqual(str(student), student.full_name)


class TestEnrollment(TestCase):
    def test_factory(self):
        enrollment = EnrollmentFactory()
        self.assertIsNotNone(enrollment)

    def test_has_student(self):
        student = StudentFactory()
        enrollment = EnrollmentFactory(student=student)
        self.assertEqual(enrollment.student, student)

    def test_has_grade_level(self):
        grade_level = GradeLevelFactory()
        enrollment = EnrollmentFactory(grade_level=grade_level)
        self.assertEqual(enrollment.grade_level, grade_level)


class testCoursework(TestCase):
    def test_factory(self):
        course_work = CourseworkFactory()
        self.assertIsNotNone(course_work)
        self.assertIsNotNone(course_work.complete_date)

    def test_has_student(self):
        student = StudentFactory()
        course_work = CourseworkFactory(student=student)
        self.assertEqual(course_work.student, student)

    def test_has_course_task(self):
        course_task = CourseTaskFactory()
        course_work = CourseworkFactory(course_task=course_task)
        self.assertEqual(course_work.course_task, course_task)
