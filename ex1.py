# prompt user for 2 integer inputs and a symbol(+, -, /, *, %, ^); if not: say unrecognized symbol

def inputInteger(num):
    while True:
        try:
            userInput = int(input(num))
        except ValueError:
            print("You have typed a non-integer value. Please try again.")
            continue
        else:
            return userInput
            break

def inputOperation(userInput):
    opers = '+,-,/,*,%,^'
    oper = opers.split(',')
    if userInput in oper:
        return True
    else:
        print("That is not a valid math operation.")

x = inputInteger("Please type an integer: ")
y = inputInteger("Please type another integer: ")
z = input("Please type one of the following math operations (+, -, / , *, %, ^): ")
inputOperation(z)



