# Calculator 

def add(n1 , n2):
    return n1 + n2

def sub(n1 , n2):
    return n1 - n2

def mul(n1 , n2):
    return n1 * n2

def div(n1 , n2):
    return n1 / n2

operations = {
    '+' : add , 
    '-' : sub,
    '*' : mul,
    '/' : div,
}


should_accumulate = True

n1 = float(input("what is the first number : "))

while should_accumulate:
   

    for symbol in operations:
        print(symbol)

    user_opn = input("enter the operation you want to perform : ")

    n2 = float(input("what is the next number : "))

    answer = operations[user_opn](n1 , n2)
    print(f"{n1} {user_opn} {n2} = {answer}")

    choice = input(f"type 'y'to continue calculating with {answer} , or type 'n' to start a new calculation : ")

    if choice == 'y':
        n1 = answer
    else:
        should_accumulate = False