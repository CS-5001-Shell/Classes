from student import Student


class StudentList:
    """
    Data about a class of students
    """

    def __init__(self, course: str, students=None):
        """Constructor
        Parameters:
          - course: string description of course (e.g., CS 5001)
          - students: optional dictionary of id -> Student mapping
        """
        pass

    def add_student(self, student: Student):
        """Add a new student to the class.
        Parameters:
          - student: Student object containing student information
        Raises an exception if student.id already exists in the
        student list.
        """
        pass

    def update_student(self, student_id: int, new_grade: float):
        """Updates a student's grade list by adding a new score.
        Parameters:
          - student_id: int representing the id of the student
          - new_grade: float representing the new score
        Raises an exception if student.id does not exist in the
        student list.
        """
        pass

    def get_student_average(self, student_id: int) -> float:
        """Returns a student's average grade.
        Parameters:
          - student_id: int representing the id of the student
        Raises an exception if student.id does not exist in the
        class.
        """
        pass

    def get_student_letter_grade(self, student_id: int) -> str:
        """Returns a student's letter grade.
        Parameters:
          - student_id: int representing the id of the student
        Raises an exception if student.id does not exist in the
        class.
        """
        pass

    def __str__(self):
        """Returns a string representation of the class.
        Note: in oder for this to work correctly you must have
        an instance variable named course that is a string and
        an instance variable named students that is a dictionary
        mapping int to Student.
        """
        result = f'{self.course}\n'
        for student in self.students.values():
            result += student.__str__()
        return result
