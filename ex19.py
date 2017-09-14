#Below line defines the function "cheese_and_crackers" and assigns parameters
# lines 4 & 5 & 9 & 10 are the output
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
#below line says thta if chese and crackers are not equal, print line8
    if cheese_count != boxes_of_crackers:
    	print("Oh shit!  Different amounts of cheese and crackers!")

    print("Man, that's enough for a party!")
    print("Get a blanket.\n")
#When the function runs the below line is printed, and values are passed to the function.
print("We can just give the function numbers directly")
cheese_and_crackers(20, 30)
#When the function runs the below line is printed, and values are passed to the function.
print("OR, we can use variables form our script:")
amount_of_cheese = 10
amount_of_crackers = 50
#When the function runs the below line is printed, and values are passed to the function.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 10)
