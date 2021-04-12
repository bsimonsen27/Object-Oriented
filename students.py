class student:
    def __init__(self, first, last, status):
        self.first = first #these are instance variables
        self.last = last
        self.status = status
        self.email = first + last + '@mail.weber.edu'

W01234 = student('Scott', 'Hazdik', 'Pass')
W01235 = student('Waldo', 'Wildcat', 'Pass')


print(W01234.first, W01234.last, W01234.email, W01234.status)
print(W01235.first, W01235.last, W01235.email, W01235.status)