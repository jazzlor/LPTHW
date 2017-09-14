name = 'Jazzy'
age = 36 # not a like
height = 54 # inches
weight = 200 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
cm = 2.54 #single cm
kg = 0.453592 #singl kg


print(f"Let's talk about {name}.")
print(f"She's {height} inches tall")
print(f"She's {weight} pounds heavy")
print(f"Actually that's not too heavy.")
print(f"She's got {eyes} eyes and {hair} hair")
print(f"Her teeth are usually {teeth} depending on the coffee")

#tHer line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

total1 = height * cm
print(f"she is {total1} cm tall")

total2 = weight * kg
print(f"She is {total2} kgs")
