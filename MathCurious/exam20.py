class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

student = Student("Jose")
student.add_mark(57)
student.add_mark(78)

print("Average mark: {}.".format(sum(student.marks) / len(student.marks)))