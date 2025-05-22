import Person as p
import Lecturer as l
import Student as s

name = input("Enter Lecturer Name: ")
nric = input('Enter Lecturer NRIC: ')

while True:
    staffid = input('Enter Staff Id: ')
    if staffid == nric:
        break
    else:
        print('Staff Id needs to be the same as NRIC')
        
hour = float(input('Enter Total Teaching Hour: '))
lecturer1 = l.Lecturer(name, nric, staffid)
lecturer1.set_total_teachinghour(hour)


name = input("Enter Student Name: ")
nric = input('Enter Student NRIC: ')
adminNo = input('Enter Student Admin No: ')

# use different approaches to validate test and exam mark
test = -1
while True:
    test = float(input('Enter Test mark: '))
    if test < 0 or test > 100:
        print('Test marks must be between 0 to 100 (inclusive)')
    else:
        break

while True:
    exam = float(input('Enter Exam mark: '))
    if exam < 0 or exam > 100:
        print('Exam marks must be between 0 to 100 (inclusive)')
    else:
        break

student1 = s.Student(name, nric, adminNo)
student1.set_test_mark(test)
student1.set_exam_mark(exam)

print(lecturer1)
print(student1)
