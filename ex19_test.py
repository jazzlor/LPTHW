def chips_and_salsa(bag_chips, jars_of_salsa):
    print(f"We have {bag_chips} bags of chips")
    print(f"Oh, look, Tim bought {jars_of_salsa} jars of salsa...")

    if bag_chips > jars_of_salsa:
        print("Dammit Tim, why didn't you get enough salsa?")

    if bag_chips < jars_of_salsa:
        print("Dammit Tim, why did you get so much salsa??")

    if bag_chips == jars_of_salsa:
        print("It's about time Tim got it right.")

chips_and_salsa(1,6)

bag_chips = 4
jars_of_salsa = 3

chips_and_salsa(3 + 4, 5 + 1)

chips_and_salsa(bag_chips + 1, jars_of_salsa + 2)
