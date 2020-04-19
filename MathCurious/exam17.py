class StudentList:
    def __init__(self):
        self.__students = []

    def add(self, student):
        if not isinstance(student, Student):
            raise TypeError("Incorrect type: tried to add a {} instead of a Student.".format(type(student)))
        self.__students.append(student)

    def pop(self):
        if len(self.__students) <= 0:
            raise EmptyListError("Tried to remove from the list but it was already empty.")
        first_element = self.__students[0]
        self.__students.remove(first_element)
        return first_element

class Student:
    def __init__(self, name):
        self.name = name

class EmptyListError(Exception):
    def __init__(self, message):
        self.message = message

student_list = StudentList()
student_list.add("John")
print(student_list)