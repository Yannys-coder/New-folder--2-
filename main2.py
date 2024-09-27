class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)
        
class student(person):
     def __init__(self, fname, lname, year):
         super(). __init__(fname, lname)
         self.year = year
x= student( "Laila", "Joseph", 2025)

x.printname()

print(x.year)
