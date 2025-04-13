class User:
    
    #constructor
    def __init__(self, user_id, username):
        print("new user being created")
        self.id = user_id
        self.username = username

user_1 = User("001")
user_1.id = "001"
user_1.username = "pogo"

print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "rans"