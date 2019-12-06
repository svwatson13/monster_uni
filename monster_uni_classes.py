class Monster():
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

class Student_Monster(Monster):
    def __init__(self, uni_id, grade = 'c'):
        self.uni_id = uni_id
        self.grade = grade

class Staff(Monster):
    def __init__(self, staff_id):
        self.staff_id = staff_id

class Building():
    def __init__(self, location):
        self.location = location

class Lecture_Theatres(Building):
    def __init__(self, hall_number):
        self.hall_number = hall_number

class Spooky_Workshop(Student_Monster, Staff, Building):
    def __init__(self, subject, students = []):
        self.subject = subject
        self.students = students
    def add_student(self, uni_id):
        self.students.append(uni_id)