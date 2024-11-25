# Write a python program to print the content of a directory using the os module. Search online for the function which does that

import os

directory_path = '/WEB-DEV-PRO 1/BackEnd-Development/Python Programming'

contents = os.listdir(directory_path)

for item in contents:
    print(item)
