# combining the name

def greet(first_name , last_name):
    name = first_name.title() + " " +  last_name.title()
    return f"hello {name}"


greeting = greet("pogo" , "lopa")

print(greeting)