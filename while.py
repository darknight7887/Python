total_numbers = 0
current_num = 0
running_total = 0

while current_num != -1:
    user_input = float(input("Please enter a number: "))
    current_num = user_input
    running_total = running_total + current_num
    total_numbers += 1

if current_num == -1:
    running_total += 1
    total_numbers -= 1
    print(f"The average of your numbers is {running_total/total_numbers}")
              
              
