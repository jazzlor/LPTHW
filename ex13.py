#The below line says from the Sys system module import the argv feature
from sys import argv
# read the WYSS section for how to run this
#This line assigns four variables for argv note - the script value is a freebie - it's the filename.
script, first, second, third = argv
#The below line prints the text between the quotes and the variables that you enter when you run the script.
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
