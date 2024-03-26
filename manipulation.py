str_manip = str(input("Please enter a sentence"))
print(len(str_manip))
last_letter = str_manip[-1:]
        
print(str_manip.replace(last_letter, "@"))
print(str_manip[:-4:-1])

new_word = str_manip[0:3] + str_manip[-2:]
print(new_word)

        
