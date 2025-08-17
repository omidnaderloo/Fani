a = int(input("Enter a number1:"))
b = int(input("Enter a number2:"))
start = min(a, b)
end = max(a, b)
if a==b:
    print(" its equal and cannot compare")
else:
    print("sodi=1")
    print("nozoli=2")
    c = int(input("Select one of them:"))
    if c == 1:
     while start < end:
             print(start + 1, end='')
             print("")
             start += 1
    if c == 2:
        while start < end:
             print(end - 1, end='')
             print("")
             end -= 1
    else:
        print("out of range")
