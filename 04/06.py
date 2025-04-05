# picking a random person to pay the bill 

import random 

friends = ["Pogo" , "Tom" , "Mony" , "Jaadu"]

num = random.randint(0,3)

pay = print(friends[num])
print(f"Today {pay} will pay the bill")