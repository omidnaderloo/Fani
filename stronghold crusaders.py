n1 = int(input("enter a number: "))
n2 = int(input("enter a number: "))
x = 0
if n1 > n2:
    x = n1 - n2
else:
    x = n2 - n1
while x >= 1:
    print(x)
    x -= 1
