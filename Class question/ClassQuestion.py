'''
ClassQuestion.py


TOTAL POINTS AVAILABLE: 50


12 points per method, 42 across whole class, 8 points for the creation of the students and the task.

--------------------------------------
Marking for methods:
--------------------------------------

12 points -  The program works flawlessly, it is commented and easy to read. The appropriate ideas to solve it, have been used.

9-11 points - The student has understood the logic and the program works for all inputs.
The code could use some improvement or it is difficult to read and understand. The appropriate ideas to solve the problem have been used.

7-8 points - The student has understood the logic and the program works for most inputs. 
The appropriate ideas to solve the problem have been used.

3-6 points - The student has understood the logic but there is some major bugs, or the program is incomplete. 
This score is also assigned for programs that execute as intended but in a 
very inefficient way (for instance, using a very long list of if statements 
when the problem could be solved easily with a loop).

1-2 points -  The student has attempted to solve the exercise but, either there is a 
logical error in the program (e.g., wrote something but it wouldn't solve the problem) 
or the program is largely incomplete.

0 points - The student has not attempted to solve the exercise or missed the point entirely 
(e.g., blank page or solved something unrelated to the question).

--------------------------------------
Marking for the creation of students:
--------------------------------------

8 points -  The program works flawlessly, it is commented and easy to read. The appropriate ideas to solve it, have been used.

6-7 points - The student has understood the logic and the program works for all inputs.
The code could use some improvement or it is difficult to read and understand. The appropriate ideas to solve the problem have been used.

4-5 points - The student has understood the logic and the program works for most inputs. 
The appropriate ideas to solve the problem have been used.

2-3points - The student has understood the logic but there is some major bugs, or the program is incomplete. 
This score is also assigned for programs that execute as intended but in a 
very inefficient way (for instance, using a very long list of if statements 
when the problem could be solved easily with a loop).

1 points -  The student has attempted to solve the exercise but, either there is a 
logical error in the program (e.g., wrote something but it wouldn't solve the problem) 
or the program is largely incomplete.

0 points - The student has not attempted to solve the exercise or missed the point entirely 
(e.g., blank page or solved something unrelated to the question).

'''



# Create a class called Student with one instance attribute called "courses"
# that is created in the constructor.
#   
#   - "courses" will be a dictionary and will start empty in the constructor 
#        but when populated later by other methods: 
#         - the keys will be string describing the name of the course (e.g. 'computing') 
#         - and the values will be a dictionary of two items
#                   1. the first item is 'year' in which the course takes place (an integer from 1 to 4)
#                   2. the second item is 'grade' (expressed with a float from 1 to 100)
#                   (e.g. {'computing': {'year': 1, 'grade': 87.5})




# Create a method called add_course(). It should:
#   - have 3 parameters: 'course_name', 'year' and grade
#   - 'grade' has a default value of "None"
#   - it should change the grade of the corresponding course in the "courses" attribute
#        - if the course exists already ask the user (via terminal) if they want to change the existing course.
#           if the user says "yes" or "y", change the grade and the year accordingly. If the grade was not specified, ask the user (via terminal) for the grade
#           if the user writes "no" or "n", ignore it. 
#           keep asking the question until the user inputs either yes/y or no/n
#        - if the course does not already exist in the dictionary, add a new entry


# Create a method called change_grade(). It should:
#   - have 2 parameters: 'course', grade
#   - it should change the grade of the course
#        - if the course exists already, change the grade accordingly
#        - if the course doesn't exist, notify the user that the course doesn't exist and ask them if they want to create one (via terminal).
#          if the user says "yes" or "y", ask for the year of the course and then add the new course accordingly,
#          if the user writes "no" or "n", ignore it. 
#           keep asking the question until the user inputs either yes/y or no/n



# Create a method called calculate_mean(). It should: 
#   - have one parameter, either a list of strings or a year (from 1 to 4):
#   - if the parameter is the year, the method returns the average of all the courses for that specific year. If there are no courses for that year, the method
#     will return "None" and print "No courses added for year {year}"
#   - if the parameter is a list of strings, the method returns the average for all courses in that string. 
#        if any of the courses in the string are not present in the attribute "courses", the method will ignore them and just return
#        the mean for the ones that are present. If none of the courses are present the method will return "None" and print "The student "



# Create 10 instances of the class Student and to each one of them assign a course "computing I" and a
# course "Mathematics". 
#   - Both of them have year 1 as the year and a random grade between 1 and 100.
#   - Write a function called "calculate_overall_mean()" that takes as input any list of students and an optional argument "course" (default None).
#       
#       -If course is not specified the function will return a dictionary with, as keys, all the courses that the students have
#        (mathematics and computing in this example, but there could be more) and as value the mean across the list students.
#       - If course is specified, the function will return the mean for that specific course across the list of students.



from matplotlib.pyplot import violinplot
from numpy.lib.function_base import average


class Student(): 

    courses = { "Computing1" : {"Year" : None , "Grade" : None}, "Mathematics" : {"Year" : None, "Grade" : None}}

    def __init__(self, course_name, year, grade = None):
        self.course_name = course_name
        self.year = year
        self.grade = grade
        

    def add_course(self, course_name, year, grade = None):
        if course_name in self.courses.keys(): 
            print("Do you want to change the existing course: yes or no?")
            if input() == "yes": 
                if grade is None: 
                    print("Please specify the grade: ...")
                    grade = input()
                    self.courses[course_name] = {"Year": year, "Grade" : grade}
                else: 
                    self.courses[course_name] = {"Year": year, "Grade" : grade}
            else: 
                pass
        else:
            self.courses[course_name] = {"Year": year, "Grade" : grade} 
    
    def change_grade(self, course_name, grade):
        if course_name in self.courses.keys():
            self.courses[course_name] = {"Year": self.year, "Grade" : grade}
        else:
            print("This course doesn't exist, would you like to create it: yes or no?")
            if input == "yes":
                print("What year applies to this course?")
                year = input()
                self.courses[course_name] = {"Year": year, "Grade" : grade}
            else: 
                pass
    
    def calculate_mean(self, input):
        if type(input) is list: 
            gradeList = []
            for i in range(len(input)): 
                values = self.courses[input[i]]
                grade = values["Grade"]
                gradeList.append(grade)
            Sum = sum(gradeList)
            average = Sum / len(gradeList)
        elif type(input) is int: 
            valueList = list(self.courses.values())
            avgList = []
            for index, item in enumerate(valueList):
                year = item["Year"]
                if year == input: 
                    valueDic = valueList[index]
                    grade = valueDic["Grade"]
                    avgList.append(grade)                
            
            
            Sum = sum(avgList)
            
            average = Sum / len(avgList)
        
        return average
        
            





Paul = Student("Computing1", 1, 89.3)
Paul.add_course("Computing1", 3,86.6)
Paul.add_course("Mathematics", 2, 97.4)
print(Paul.courses)
print(Paul.calculate_mean(2))
