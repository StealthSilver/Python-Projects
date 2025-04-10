# modifying a local variable globally

enemies = 1

def increase_enemies():
    global enemies
    enemies += 2
    print(f"enemies inside the function {enemies}")


increase_enemies()
print(f"enemies outside the function {enemies}")