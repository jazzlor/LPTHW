# print whatever string is passed in
def PrintWord(word):
    print("Word: %s") % word;
# an array of strings
words=['one', 'two', 'three', 'four'];
# go through 'words' array one by one
# and pass them into PrintWord for printing
for word in words:
    
    PrintWord(word)
