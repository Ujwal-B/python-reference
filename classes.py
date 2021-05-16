class student:
    '''
    self keyword is used to assign values to the object. __init__ acts like a constructor
    __init__ always has to have 'self' as a parameter
    '''
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    
    def is_doing_honors(self):      # custom function
        if self.gpa >= 7.5:
            return True

student1 = student("Abhi", "Comp Sci", 9.0)
student2 = student("Aakash", "MBA", 8.9)

if student1.is_doing_honors():
    print("Student is pursuing an honors degree")
else:
    print("Student is pursuing a normal degree")

