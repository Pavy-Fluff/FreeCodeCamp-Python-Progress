# FreeCodeCamp - Python Basics
# my "better" report_card.py

name = "Pavy"
age = 16
position = "Home"
salary = 0
learning = "IT"
experience = str(1) + ' year'
hobby = "tapping"

# Ugly way to present yourself

introduction = name + ' ' + str(age) + ' ' + position + ' ' + str(salary) + ' ' + learning + ' ' + str(experience) + ' ' + hobby 
print(introduction)

# Better way

introduction = f'Name: {name} | Age: {age} | Position: {position} | Salary: {salary} | Learns: {learning} | Experience: {experience} | Hobby: {hobby}'
print(introduction)
