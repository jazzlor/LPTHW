#the below linesays that the module named sys should import the thing named argv
from sys import argv
#the below line says that the script and the filename equal argv
script,filename = argv
#The below line assigns the value "txt" to perform the open(filename) action
txt = open(filename)
#The below line will print the text in green, and display the filename you entered.
print(f"Here's your file{filename}:")
##The below line will display the text of the file
print(txt.read())

#The below line prints what is in green
print("Type the filename again:")

#The below line  will ask for the filename  and assign it to "file_again"
file_again = input("> ")
#The below line says that txt_again will peform the action of opening the file designated in file_again
txt_again = open(file_again)
#The below line will print the text.
print(txt_again.read())
