class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    TYPES = ('school', 'college', 'university')

    def __init__(self, name, student_type):
        super().__init__(name)
        if student_type not in Student.TYPES:
            raise TypeError("Incorrect student type, entered {} but expected one of {}.".format(student_type, Student.TYPES))
        self.student_type = student_type

student = Student("John", "college")
print(student.name)
print(student.student_type)