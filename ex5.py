#The below line assigns a value to "types_of_people"
types_of_people = 10
#the below line prints the text while inserting the value for "types_of_people"
x = f"There are {types_of_people} types of people."
#the below line assigns a value to "binary"
binary = "binary"
#The below line assigns a value to "do_not"
do_not = "don't"
#The below line assigns a value to "y" inserts the value for "binary" and "do_not"
y = f"Those who know {binary} and those who {do_not}."

#The below line prints line 4 and inserts the value for "types_of_people"
print(x)
#the below line prints line 10 and inserts the value for "binary" and "do_not"
print(y)
#the below line prints "I Said" and inserts the text and value from line 4
print(f"I said: {x}")
#the below line prints "I also said" and inserts the text and value from line 10
print(f"I also said '{y}'") #string in string
#the below line assigns a value to "hilarious"
hilarious = False
#the below line assigns a value to joke_evaluation - don't know what the empty curly braces are
joke_evaluation = "isn't that joke so funny?! {}"
#prints joke_evaluationand hilarious - not sure what .format does
print(joke_evaluation.format (hilarious))
#below line assigns a value to w
w = "This is the left side of..."
#below line assigns a value to e
e = "a string with a right side"
#below line prints the values of w & e in order
print(w + e)
