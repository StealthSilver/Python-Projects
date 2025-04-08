# Docstrings -> they are used to write a brief about hte function you have defined


def greet(first_name , last_name):
    name = first_name.title() + " " +  last_name.title()
    return f"hello {name}"


greeting = greet("pogo" , "lopa")

print(greeting)