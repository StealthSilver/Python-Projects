class User:
    
    #constructor
    def __init__(self, user_id):
        print("new user being created")
        self.id = user_id

user_1 = User()
user_1.id = "001"
user_1.username = "pogo"

print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "rans"