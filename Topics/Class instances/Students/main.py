class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.student_id = self.name[0] + self.last_name + str(self.birth_year)


student_firstname = input()
student_surname = input()
student_birthyear = input()
student = Student(student_firstname, student_surname, student_birthyear)
print(student.student_id)
