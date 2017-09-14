#The below line says that the module named sys will import the thing called argv
from sys import argv
#The below line says script,filename = argv
script, filename = argv
#The below line prints the greentext & inserts the filename that you entered when running the program
print(f"We're going to erase {filename}.")
#The below line prints the greentext
print("If you don't want that, hit CTRL-C (^C).")
#The below line prints the greentext
print("If you do want that, hit RETURN")
#The below line prints the greentext and waits for an input from the user
input("?")
#The below line prints the greentxt
print("Opening the file...")
#The below line opens the file, and prepares to write to it.
target = open(filename, 'w')
#The below line prints the greentext
print("Truncating the file. Goodbye!")
#The below line erases the file using the "truncate" command
target.truncate()
#Below line prints the greentext
print("Now I'm going to ask you for three lines.")
#below line assigns the line1 variable. The variable displays the greentext and awaits an input
line1 = input("line 1: ")
#Same as 23
line2 = input("line 2: ")
#Same as 25
line3 = input("line 3: ")
#Below line prints the greentext
print("I'm going to write these to the file.")
#Below line writes line1 to the file
target.write(line1)
#Below line writes a new line to the file
target.write("\n")
#below line writes line2 to the file
target.write(line2)
#below line writes a new line to the file
target.write("\n")
#below line writes line3 to the file
target.write(line3)
#below line writes a newline to the file
target.write("\n")
#Below line prints the greentext
print("And finally, we close it.")
#below line closes the file
target.close()
