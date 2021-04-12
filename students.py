class student: 
    def __init__(self, first, last, status):
        self.first = first #these are instance variables
        self.last = last
        self.status = status
        self.email = first + last + '@mail.weber.edu'

    #Behavior
    def printStudentInfo(self):
        print('Full Name:', self.first, self.last, '\nEmail:', self.email, '\nStatus:', self.status, '\n')

W01234 = student('Scott', 'Hazdik', 'Pass')
W01235 = student('Waldo', 'Wildcat', 'Pass')

W01234.printStudentInfo()
W01235.printStudentInfo()