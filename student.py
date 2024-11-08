class Student:
	"""
	Data about a single student.
	"""
	
	def __init__(self, name, id, grades=None):
		"""Constructor
		Parameters:
		  - name: student's name
		  - id: student's id
		  - grades: optional list of scores		
		"""
		pass

	def add_grade(self, grade):
		"""Append a new score onto the grades list.
		"""
		pass

	def get_average(self):
		"""Return the mean across all scores in the grades list.
		"""
		pass

	def get_letter_grade(self):
		"""Return the mapping from average score to letter grade.
		Greater than or equal to 90 is an A.
		Greater than or equal to 80 is a B.
		Greater than or equal to 70 is a C.
		All other scores earn an F.
		"""
		pass

	def __str__(self):
		"""Returns a string representation of the Student.
		Note: in order for this to work correctly you must have
		an instance variable named name that is a string, and 
		instance variable named id that is an int, and an
		instance variable named grades that is a list of float.
		"""
		result = f'\t{self.name} - {self.id}:\n\t\t'
		for grade in self.grades:
			result += str(grade) + ' '
		result += '\n'
		result += f'\t\tAverage: {self.get_average()} - {self.get_letter_grade()}'
		result += '\n'
		return result