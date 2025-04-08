# Docstrings -> they are used to write a brief about the function you have defined


def greet(first_name , last_name):
    """Take a first and a last name and format it to return the tile case version if the name"""
    name = first_name.title() + " " +  last_name.title()
    return f"hello {name}"


greeting = greet("pogo" , "lopa")

print(greeting)