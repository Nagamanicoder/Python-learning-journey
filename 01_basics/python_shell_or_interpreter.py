# entering the python shell in various types of OS
# windows -> IDLE
# mac & linux -> python3
# command line interface -> python 

# opening the integrated terminal by right clicking over the folder

# ctrl + d and ctrl + z is used tot erminate from the terminal 
# ctrl + d is used to completely terminate the terminal 
#ctrl + z is used to susupend the terminal

# code written in the terminal cannot be saved

#import a file into another code using the import keyword
# in the commmand shell, using the filename.method name

# >>> import print_anything
# Hello Python Programming
# solitude
# >>> print_anything.Hello('mani')
# mani

# after changing the code and started to use the things that are changed after importing 
# then they cannot be accessed and an attribute error will come
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'print_anything' has no attribute 'state_one'

# so to make it we have
# > re import the the file
# > close the terminal and restart

# another method is using the following 
# from importlib import reload
# reload(file_name)
