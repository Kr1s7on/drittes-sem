import Person

class Student(Person.Person):
    def __init__(self, name, nric, adminNo):
        Person.Person.__init__(self, name, nric)
        self.__admin_No = adminNo
        self.__test_Mark = 0
        self.__exam_Mark = 0

    def get_admin_no(self):
        return self.__admin_No
    def get_test_mark(self):
        return self.__test_Mark
    def get_exam_mark(self):
        return self.__exam_Mark

    def set_admin_no(self, adminNo):
        self.__admin_No = adminNo
    def set_test_mark(self, testMark):
        self.__test_Mark = testMark
    def set_exam_mark(self, examMark):
        self.__exam_Mark = examMark

    def computeFinalMark(self):
        return (self.__test_Mark + self.__exam_Mark) / 2

    def __str__(self):
        s = '%s, Admin No: %s final mark is %.2f' %(self.get_name(), self.get_admin_no(), self.computeFinalMark())
        return s