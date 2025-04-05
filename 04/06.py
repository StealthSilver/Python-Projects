# picking a random person to pay the bill 

import random 

friends = ["Pogo" , "Tom" , "Mony" , "Jaadu"]
print(len(friends))

num = random.randint(0,3)

# we can also use random.choice(friends) to get the random name

pay = friends[num]
print(f"Today {pay} will pay the bill")