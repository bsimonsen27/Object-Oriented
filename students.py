class student: 
    grade = 0
    passing_grade = 75
    award_credit = False

    def __init__(self, first, last):
        self.first = first #these are instance variables
        self.last = last
        self.email = first + last + '@mail.weber.edu'

    #Behavior
    def printStudentInfo(self):
        print('Full Name:', self.first, self.last, '\nEmail:', self.email, '\nGrade:', self.grade, 'Award Credit:', self.award_credit,'\n')

    def setGrade(self, grade):
        self.grade = grade
        if self.grade < self.passing_grade:
            self.award_credit = False
        else:
            self.award_credit = True



W01234 = student('Scott', 'Hazdik')
W01235 = student('Waldo', 'Wildcat')

print('Start of the Semester')
print('---------------------')
W01234.printStudentInfo()
W01235.printStudentInfo()

print('Middle of the Semester')
print('---------------------')

W01234.setGrade(45)
W01235.setGrade(75)

W01234.printStudentInfo()
W01235.printStudentInfo()

print('End of the Semester')
print('---------------------')
W01234.printStudentInfo()
W01235.printStudentInfo()



