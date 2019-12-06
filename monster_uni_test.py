from monster_uni_classes import *
from monster_uni_run import *

# Testing creation of uni_id and grade for each student
print('This is a test of whether we can succesfull add uni id and grade to a student')
print(Student_Monster(4756, '2:1').uni_id == 4756)
print(Student_Monster(4756, '2:1').grade == '2:1')

# Testing list of workshops
print('\nThis is the list of workshops:')
print(workshops)

# Testing creation of workshop
print('\nThis is a test of creating a workshop and designating a subject:')
print(Spooky_Workshop('Scaretime').subject == 'Scaretime')
Spooky_Workshop('Scaretime')

# Testing enrollment of students to workshops
'\nThis is a test of adding students to workshops'
spooktober = Spooky_Workshop('Scaretime')
spooktober.add_student(4756)
print(spooktober.students == [4756])