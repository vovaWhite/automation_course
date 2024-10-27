class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self):
        new_average_grade = input('Enter new average grade: ')
        self.average_grade = new_average_grade

    def __str__(self):
        return f"Student: {self.name}, {self.surname}, age: {self.age}, average grade: {self.average_grade}"


first_student = Student("Vova", "Butynets", 26, 50)

print(first_student)

first_student.change_average_grade()

print(first_student)
