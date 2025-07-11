#!/usr/bin/env python3
# Author ID: jgylagan

class Student:

    # Define the name and student ID number (which is a string) when a student object is created, ex. student1 = Student('john', '025969102')
    def __init__(self, name, number):
        self.name = name
        self.number = str(number) # incase of number type error
        self.courses = {}

    # Display student name and number
    def displayStudent(self):
        print('Student Name: ' + self.name)
        print('Student Number: ' + self.number)

    # Add a new course and grade to students record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate the grade point average of all courses and display it
    def displayGPA(self):
        gpa = 0.0
        for course in self.courses.keys():
            gpa = gpa + self.courses[course]
        print('GPA of student ' + self.name + ' is ' + str(gpa / len(self.courses)))


# Main code block
if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', 123456)
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())