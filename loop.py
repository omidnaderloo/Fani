a = int(input("enter a number: "))
total = 0
i = 0
if a >= 1:
    while i < a:
        total += i
        i += 1
    print(total)
else:
    print("error")
