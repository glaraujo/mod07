# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:04:30 2024

@author: nm108e
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Gustavo Limongi Araujo, 2/26/2024, Assignment07)
#   RRoot,1/1/2030,Created Script
#   <Gustavo L. Araujo>,<02/26/2024>,<Assignment 07>
# ------------------------------------------------------------------------------------------ #
"""


import json

class FileProcessor:
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            with open(file_name, 'r') as file:
                student_data.extend(json.load(file))
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Starting with an empty list.")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            with open(file_name, 'w') as file:
                json.dump(student_data, file, indent=4)
            print(f"Data saved to '{file_name}'")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")

class IO:
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        if error:
            print(f"Error: {message} - {error}")
        else:
            print(f"Error: {message}")

    @staticmethod
    def output_menu(menu: str):
        print(menu)

    @staticmethod
    def input_menu_choice():
        return input("Enter your choice: ")

    @staticmethod
    def output_student_courses(student_data: list):
        for student in student_data:
            print(f"Student: {student['student_first_name']} {student['student_last_name']} - Course: {student['course_name']}")

    @staticmethod
    def input_student_data(student_data: list):
        try:
          student_first_name=input("Enter Student's First Name:")
          if not student_first_name.strip():
              raise ValueError ("First name can not be empty")
          
          student_last_name = input("Enter student's last name: ")
          if not student_last_name.strip():
              raise ValueError ("Last Student Name can not be empty")
              
          course_name = input("Enter course name: ")
        
          student_data.append({'student_first_name': student_first_name, 'student_last_name': student_last_name, 'course_name': course_name})
        except Exception as e:
            IO.output_error_messages("An error occurred while outputing student data",e)
              

class Person:
    def __init__(self, student_first_name: str = "", student_last_name: str = ""):
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name

class Student(Person):
    def __init__(self, student_first_name: str = "", student_last_name: str = "", course_name: str = ""):
        super().__init__(student_first_name, student_last_name)
        self.course_name = course_name

# Constants
MENU = """---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------"""
FILE_NAME = "Enrollments.json"
students = []

# Load initial data
FileProcessor.read_data_from_file(FILE_NAME, students)

# Main loop
while True:
    IO.output_menu(MENU)
    choice = IO.input_menu_choice()

    if choice == '1':
        IO.input_student_data(students)
    elif choice == '2':
        IO.output_student_courses(students)
    elif choice == '3':
        FileProcessor.write_data_to_file(FILE_NAME, students)
    elif choice == '4':
        break
    else:
        IO.output_error_messages("Invalid choice. Please select a valid option.")

print("Program exited.")
