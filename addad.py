
number=45
"""salam mitonid hatta addad ro az vorody vared konid
number=int(input("Input the number"))
"""
tries=0

while True:
    guess1=int(input("Input the number"))
    tries=tries+1
    if guess1<100 or guess1>0:
        if guess1<number:
            print("Guess the higher number")
        elif guess1>number:
            print("Guess the lower number")
        else:
             print(f"You guessed the number,number is:{guess1} ")
    else:
        print("Your number is out of the range")