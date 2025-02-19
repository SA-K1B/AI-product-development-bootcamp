# list of students
# add the names Abdul , Dildar to the list of students

students = ["Alice", "Bob","Abdul", "Charlie", "Dildar"]

# print names starting with 'A' or 'D'
for student in students:
    if student.startswith('A') or student.startswith('D'):
        print(student)