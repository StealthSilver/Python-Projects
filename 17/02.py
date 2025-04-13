class User:
    
    #constructor
    def __init__(self, user_id, username):
        print("new user being created")
        self.id = user_id
        self.username = username
        # default value for a object
        self.followers = 0

user_1 = User("001" ,"pogo")
print(user_1.username)
print(user_1.followers)

user_2 = User("002", "rans")
print(user_2.id)