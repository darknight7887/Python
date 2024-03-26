pattern = "*"
step = 1

for i in pattern:
    while step <= 4:
        print(pattern * step)
        step += 1
    if step == 5:
        while step <= 5 and step > 0:
            print(pattern * step)
            step -= 1           