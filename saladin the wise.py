num=int(input("enter a number"))
m=7
x=8
match num:
    case 1|3|5 if m==7:
        print('odd')
    case 2|4|6 if x==8:
        print('even')
    case _:
        print('error')