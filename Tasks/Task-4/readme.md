# Task 4 - Person and Student Classes

## Description
This task demonstrates the use of class inheritance in Python. It includes two classes: `Person` and `Student`, where `Student` inherits from `Person`. Each class has an `introduce()` method that outputs a specific message.

## Classes
- **Person**: A base class with an `introduce()` method that prints "I am a person."
- **Student**: A subclass of `Person` that overrides the `introduce()` method to print "I am a student."

## Usage
```python
# Create instances of Person and Student
person = Person()
student = Student()

# Call the introduce method
person.introduce()  # Output: I am a person.
student.introduce()  # Output: I am a student.
```

## Conclusion
This task demonstrates the concepts of inheritance and polymorphism in Python. The `Student` class inherits from `Person` and overrides the `introduce()` method to provide its own implementation.
