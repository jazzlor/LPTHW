from sys import argv
script, filename = argv
txt = open(filename)

print(f"Here's your {filename}!")
print(txt.read())
