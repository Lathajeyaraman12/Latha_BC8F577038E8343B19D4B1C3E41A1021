class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

# Example usage:
# Creating a list of Student objects
students = [
  Student("John Doe", "A001", 3.8),
  Student("Alice Smith", "A002", 3.9),
  Student("Bob Johnson", "A003", 3.7),
  # Add more students as needed
]

# Sorting the list of students based on CGPA
sorted_students = sort_students(students)

# Displaying the sorted list
for student in sorted_students:
  print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
