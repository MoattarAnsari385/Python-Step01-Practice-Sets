# Label the program in problem 4 with comments.

import os
# Select the directory whose content you want to list
directory_path = '/WEB-DEV-PRO 1/BackEnd-Development/Python Programming'

# Use the os module to list the directory content
contents = os.listdir(directory_path)

# Print the content of the directory
for item in contents:
    print(item)