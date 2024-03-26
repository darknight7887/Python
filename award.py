swimming_time = float(input("Enter swimming time in minutes"))
cycling_time = float(input("Enter cycling time in minutes"))
running_time = float(input("Enter running time"))
total_time = float(swimming_time + cycling_time + running_time)

print("Your total time is {} minutes".format(total_time))

if total_time <= 100:
    print("Award received: provincial colours")
elif total_time >= 101 and total_time <= 105:
    print("Award received: provincial half colours")
elif total_time >= 106 and total_time <= 110:
    print("Award received: provincial scroll")
else:
    print("No award received")
