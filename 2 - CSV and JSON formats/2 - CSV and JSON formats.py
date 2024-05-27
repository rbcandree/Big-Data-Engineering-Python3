"""
Solve the exercises:

1. Python module os contains some important operating system features that we need while handling files in Python.
a) Import the module and use os.getcwd to get the current working directory and print that on screen.
b) Afterward change the working directory with os.chdir("path_to_the_new_directory").
c) Use os.listdir() to check the contents of your current working directory.
"""
import os
import json
import requests

# 1. a) Solution: 
def solution_1a():
    current_working_directory = os.getcwd()
    print(f"The current working directory is: {current_working_directory}")

# 1. b) & c) Solution:
# Need to use a 'raw' string with double or forward slashes instead:
# r 'C:\Users\Public'
#   'C:\\Users\\Public'
#   'C:/Users/Public' - for Linux OS
def solution_1bc():
    os.chdir('C:\\Users\\username\\Downloads')
    new_working_directory = os.getcwd()
    print(f"The new working directory is: {new_working_directory}")

    contents = os.listdir(new_working_directory)
    print(f'Contents of the new working directory:\n{contents}')
"""
2. Reading CSV files
Let's assume we have a file grades.csv, which contains names of students and the grades they received on some courses.
';' is used as the csv delimiter in this file. The file is in the following format:

Paul;5;4;5;3;4;5;5;4;2;4
Beth;3;4;2;4;4;2;3;1;3;3
Ruth;4;5;5;4;5;5;4;5;4;4

Implement a program that: 
- reads through the data;
- calculates average grade for each student;
- calculates overall average of grades for the whole class. 

The program outputs the students name, their grades and the average. 
The program also outputs the overall average of grades for whole class. 
You can use the previous 3 students grades as test input.

Expected output:
Grades for Paul: 5 4 5 3 4 5 5 4 2 4
Average for Paul: 4.1
Grades for Beth: 3 4 2 4 4 2 3 1 3 3
Average for Beth: 2.9
Grades for Ruth: 4 5 5 4 5 5 4 5 4 4
Average for Ruth: 4.5
*****
Average of the class: 3.83
"""
# 2. Solution:
def solution_2():
    with open('grades.csv') as new_file:    # We are open grades.csv and handle the file as a new_file
                                            # Unlike 'open()', where we have to close the file with the close() method, 
                                            # the 'with open() as ...:' method closes the file for us without us telling it to.
        avg_grades_sum = 0
        student_count = 0

        for line in new_file:               # ... going through the lines in a new_file with a for loop
            line = line.replace('\n', '')   # replace() method replaces a specified phrase with another specified one.
                                            # string.replace(oldvalue, newvalue)
                                            # \n (new line)  will be replaced with an empty space (whitespace)
            parts = line.split(";")         # splits a string into a list where each word is a list item: string.split("separator")
                                            # .split() method takes the separator character(in our case: ';') as a string argument, 
                                            # and returns the contents of the target string as a list of strings, separated at ';'.
                                            # We can specify the separator, default separator is any whitespace.
            name = parts[0]                 # takes 1st item from the parts-list
            grades = parts[1:]              # takes from 2nd up to the last item from the parts-list

            print(f'\nGrades for {name}:', *grades, sep = ' ')

            avg_grade = sum([int(i) for i in grades])/len(grades)
            avg_grades_sum += avg_grade

            print(f'\nAverage for {name}:', avg_grade)

            student_count += 1
        print("\n*****\n")
        class_avg = round(avg_grades_sum/student_count, 2)
        print('Average of the class:', class_avg, '\n')

# The str.replace("old", "new") method is used to replace the substring old with the string new. 
# This method returns a new copy of the string with the replacement. The original string is unchanged.

# The str.strip("parameter") method will return a copy of the string; 
# will delete any character at the beginning or end of the string that matches "any" character in the parameter we put in the strip function. 
# If no arguments are given the default is to strip whitespace characters.


# 3. Implement a program that opens weather-data.json shared in itslearning. 
# You can open this file from your own hard drive like this:

# import json
# with open('d:\\username\\yourfolder\\weather-data.json') as fh:
# data =json.load(fh)

# *notice the use of the escape character \ in front of the directory path steps.
# Find out programmatically how many KUITUVASTE_SUURI_1 measurements have been made. 
# You may need to have a look at the json file to find out how to handle it in Python.

# 3. Solution:
def solution_3():
    with open('C:\\Users\\username\\Downloads\\weather-data.json') as file_handling:
        data =json.load(file_handling)
        #formatted_data = json.dumps(data, indent = 2, separators = (", ", " = "))
    counter = 0
    for element in data['weatherStations']:
        for element1 in element['sensorValues']:
            if element1['name'] == 'KUITUVASTE_SUURI_1':
                counter += 1
                break
    
    print("The KUITUVASTE_SUURI_1 measurements have been made: {} time(s)".format(counter))

# 4. Acquire the JSON file from: https://jsonplaceholder.typicode.com/todos
# Implement a function that explores the form of the JSON file and outputs the following information:
# - The keys used in the dictionary;
# - The number of completed tasks;
# - The number of tasks with the word "delectus" in their title.

# The related user information can be found from: https://jsonplaceholder.typicode.com/users
# Use these 2 JSON files and programmatically find out the names of the users with the most completed tasks. 
# You can assume that the id in the users-JSON refers to the userID in the todos-JSON.

# 4. Solution:
response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
response_users = requests.get('https://jsonplaceholder.typicode.com/users')
data_todos = response_todos.json()
data_users = response_users.json()

def solution_4a(data_todos):
    # The keys used in the dictionary
    keys_lst = []  
    for element in data_todos[0:1]:
        for key in element.keys():
            keys_lst.append(key)
    keys_lst_str = ", ".join(str(element) for element in keys_lst)
    print("The keys used in the dictionary: " + keys_lst_str)

    # The number of completed tasks
    counter = 0
    for element in data_todos:
        if element['completed'] == True:
            counter += 1
    print(f"The number of completed tasks: {counter}")

    # The number of tasks with the word "delectus" in their title
    delectus = 0
    for element in data_todos:
        if 'delectus' in element['title']:
            delectus += 1
    print(f"The number of tasks with the word 'delectus' in their title: {delectus}")

def solution_4b (data_todos, data_users):
    # data_todos update
    for element_todos in data_todos:
        for element_users in data_users:
            if element_todos['userId'] == element_users['id']:
                element_todos.update(name = element_users['name'])
            else:
                continue
    #print(todos_data)
    
    new_obj = {}
    
    # users efficiency (todos_data):
    for element_todos in data_todos:
        value = 1
        if element_todos['completed'] == True:
            try:
                new_obj[element_todos['name']] += value
            except KeyError:
                new_obj[element_todos['name']] = value
        else:
            continue
    #print(new_obj)

    # The names of the users with the most completed tasks
    horses = []
    for key in new_obj:
        if new_obj[key] == max(new_obj.values()):
            horses.append(key)
    horses_str = ", ".join(str(name) for name in horses)
    #print(horses)
    print("The names of the users with the most completed tasks: " + horses_str)

if __name__ == '__main__':
    solution_1a()
    solution_1bc()
    solution_2()
    solution_3()
    solution_4a(data_todos)
    solution_4b(data_todos, data_users)