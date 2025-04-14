# Callback Functions 

def add(n1 , n2):
    return n1 + n2 

def substract(n1 , n2):
    return n1 - n2 

def multiply(n1, n2):
    return n1 * n2 

def divide(n1 , n2):
    return(n1 / n2)

# func is hte callback function
def calculate(n1 , n2 , func):
    return func(n1 , n2)


result = calculate(2,3,multiply)
print(result)