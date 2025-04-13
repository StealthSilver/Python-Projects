# Defining a class named 'User' and setting the methods

class User:
    
    
    def __init__(self, user_id, username):
        print("new user being created")
        
        self.id = user_id
        self.username = username
        self.followers = 0

    def follow(self, user):
        user.followers += 1
        user.following += 1

user_1 = User("001" ,"pogo")
user_2 = User("002", "rans")


user_1.follow(user_2)
print(user_1.followers)
print(user_1.followers)
print(user_2.followers)
print(user_2.followers)
