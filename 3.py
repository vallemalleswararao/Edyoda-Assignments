class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

# Example usage
student = Student()
student.setName("John Doe")
student.setRollNumber(12345)

print("Name:", student.getName())
print("Roll Number:", student.getRollNumber())