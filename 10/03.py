# multiple function calls

def fun_1(text):
    return text + text

def fun_2(text):
    return text.title()

output = fun_2(fun_1("hello"))
print(output)