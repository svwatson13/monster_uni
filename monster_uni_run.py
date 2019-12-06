from monster_uni_classes import *
workshops = ['Spooktober', 'NervyNovember', 'MayDay']
Sam = Student_Monster(4756, '2:1')
print(Sam.uni_id)
print(Sam.grade)
spooktober = Spooky_Workshop('Scaretime')
print(spooktober.subject)
spooktober.add_student(4756)
spooktober.add_student(7856)
print('Spooktober subject:', spooktober.subject, '\nStudents:', spooktober.students)



