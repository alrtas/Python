



print("---------------------")
print("   Hello, welcome    ")
print("---------------------")
print(" ")
print(" ")
print(" ")
print(" ")
print(" Choose between the following options: ")
print("  Sing up a new student:               (1) ")
print("  Get a file from a student:           (2) ")

choice = input("-> :")

print(choice) #debug



#------Class, new student

class newStudy:
    def __init__(self, name, age, address, MathGrade, PhyGrade, IngGrade):
        self.name = name
        self.age = age
        self.address = address
        self.MathGrade = MathGrade
        self.IngGrade = IngGrade
        self.PhyGrade = PhyGrade

        sumGrade = IngGrade+PhyGrade+MathGrade
        grade = sumGrade/3

        self.grade = grade



    def getName(self):
        print(" ")
        print ("The name of the student is: "+ self.name)
    def getAge(self):
        print(" ")
        print ("The age of the student " + self.name + "  is: "+ self.age)
    def getAddress(self):
        print(" ")
        print ("The ZIP code from the student " + self.name + " is: " + self.address)
    def getMathGrade(self):
        print(" ")
        print ("The grade of the student " + self.name + " in Math is: " + self.MathGrade)
    def getIngGrade(self):
        print(" ")
        print ("The grade of the student " + self.name + "  in inglish is: " + self.IngGrade)
    def getPhyGrade(self):
        print(" ")
        print ("The grade of the student " + self.name + "  in Physis is: " + self.PhyGrade)

    def getGrade(self):
        print(" ")
        print("The grade of the student " + self.name + "  in average is: " + self.grade)


# choice
if choice == 1:
    print(" ")
    print(" ")
    print ("Sing up a new student") #debug
    studentName = input("Student name: ")
    studentAge = input("Student age:  ")
    studentAddress = input("Student ZIP CODE:  ")
    studentMathGrade = input("Student math grade: ")
    studentPhiGrade = input("Student Physis grade: ")
    studentIngGrade = input("Student Inglish grade: ")

elif choice == 2:
    print(" ")
    print(" ")
    print ("Get a file from a student") #debug
else:
    print(" ")
    print(" ")
    print("Wrong option, try again")




