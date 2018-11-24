
class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []
        print("{} 학생 ".format(name))
    def addMarks(self, mark):
        self.marks.append(mark)
    def avg(self):
        return sum(self.marks) / len(self.marks)
    
        

