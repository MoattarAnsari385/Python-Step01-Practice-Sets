#  Write a Python program to list all the Python files (.py) in the current directory and print their names.

import os

directory_path = "/WEB-DEV-PRO 1/BackEnd-Development/Python Programming/Step01-Practice Sets"

content = os.listdir(directory_path)

for item in content:
    if item.endswith('.py'):
        print(item)  # Print the name of the Python file
