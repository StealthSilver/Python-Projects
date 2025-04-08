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

n1 = input("what is the first number : ")
for symbol in operations:
    print(symbol)
user_opn = input("enter the operation you want to perform : ")

print(operations["*"](4,8))