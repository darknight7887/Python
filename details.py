#Ask the user for their name, age, house number and street name and store these as variables with corresponding names
#Output all information of user in a single sentence

name = input("What is your name?")
age = input("How old are you?")
house_number = input("What is your house number?")
street_name = input ("What is your street name?")

print("This is {}. They are {} years old and lives at house number {} on {}".format(name, age, house_number, street_name))