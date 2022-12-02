class Student:
    
    institute = 'Besant' # class variable
    
    def __init__(self, m1, m2, m3):
        #instance variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    #instance method    
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    #class method
    @classmethod # special decorators
    def getInstitute(cls):
        #cls is a keyword to refer class 
        return cls.institute
    
    #static method
    @staticmethod # special decorators
    def info():
        # in static method, no need to use self as we don't want to refer to the object or any variables
        print("Welcome to Python class")
        
s1 = Student(34, 47, 23)
s2 = Student(17, 89, 44)

print(s1.avg())
print(Student.getInstitute())
Student.info()
