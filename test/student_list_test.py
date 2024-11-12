import unittest
from student import *
from student_list import *
import pycodestyle

class TestStudentList(unittest.TestCase):

    def test_init_no_param(self):
        sl = StudentList('CS 5002')
        self.assertEqual(sl.course, 'CS 5002')
        self.assertEqual(len(sl.students), 0)

    def test_add_student_does_not_exist(self):
        sl = StudentList('CS 5001')
        s = Student('Albert Gorden', 98765, [90, 92])
        sl.add_student(s)
        self.assertAlmostEqual(sl.get_student_average(98765), 91)        

    def test_add_student_exists(self):
        sl = StudentList('CS 5001')
        s1 = Student('Albert Gorden', 98765, [90, 92])
        s2 = Student('Bethany Wang', 98765)
        sl.add_student(s1)
        self.assertRaises(Exception, sl.add_student, s2)        

    def test_update_student_length(self):
        sl = StudentList('CS 5001')
        s1 = Student('Albert Gorden', 98765, [90, 92])
        sl.add_student(s1)
        sl.update_student(98765, 91)
        self.assertEqual(len(sl.students[98765].grades), 3)        

    def test_get_student_average(self):
        sl = StudentList('CS 5001')
        s1 = Student('Albert Gorden', 98765, [90, 92, 91])
        sl.add_student(s1)
        self.assertAlmostEqual(sl.get_student_average(98765), 91)        

    def test_get_student_average_empty_list(self):
        sl = StudentList('CS 5001')
        s1 = Student('Albert Gorden', 98765)
        sl.add_student(s1)
        self.assertAlmostEqual(sl.get_student_average(98765), 0)        

    def test_get_student_letter_grade(self):
        sl = StudentList('CS 5001')
        s1 = Student('Albert Gorden', 98765, [90, 92, 91])
        sl.add_student(s1)
        self.assertEqual(sl.get_student_letter_grade(98765), 'A')        

    def test_get_student_letter_grade_empty_list(self):
        sl = StudentList('CS 5001')
        s1 = Student('Albert Gorden', 98765)
        sl.add_student(s1)
        self.assertEqual(sl.get_student_letter_grade(98765), 'F')        

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['student_list.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()