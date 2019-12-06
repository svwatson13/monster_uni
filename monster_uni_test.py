from monster_uni_classes import *
print(Student_Monster(4756, '2:1').uni_id == 4756)

print(Spooky_Workshop('Scaretime').subject == 'Scaretime')
Spooky_Workshop('Scaretime')

spooktober = Spooky_Workshop('Scaretime')
spooktober.add_student(4756)
print(spooktober.students == [4756])