class Person:
    def introduce(self):
        print("I am a person.")

class Student(Person):
    def introduce(self):
        print("I am a student.")

person = Person()
student = Student()

person.introduce()  # Output: I am a person.
student.introduce()  # Output: I am a student.