import Person as p
import Lecturer as l
import Student as s

name = input("Enter Lecturer Name: ")
nric = input('Enter Lecturer NRIC: ')
staffid = input('Enter Staff Id: ')
hour = float(input('Enter Total Teaching Hour: '))
lecturer1 = l.Lecturer(name, nric, staffid)
lecturer1.set_total_teachinghour(hour)


name = input("Enter Student Name: ")
nric = input('Enter Student NRIC: ')
adminNo = input('Enter Student Admin No: ')
test = float(input('Enter Test mark: '))
exam = float(input('Enter Exam mark: '))

student1 = s.Student(name, nric, adminNo)
student1.set_test_mark(test)
student1.set_exam_mark(exam)

print(lecturer1)
print(student1)



