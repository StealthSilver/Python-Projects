# Defining a class named 'User' and setting the attributes
class User:
    
    # Constructor method that is called automatically when a new object of the class is created
    def __init__(self, user_id, username):
        print("new user being created")
        
        # Assign the provided user_id to the 'id' attribute of the object
        self.id = user_id
        
        # Assign the provided username to the 'username' attribute of the object
        self.username = username
        
        # Set a default value of 0 for the 'followers' attribute of the object
        self.followers = 0

user_1 = User("001" ,"pogo")

print(user_1.username)
print(user_1.followers)


user_2 = User("002", "rans")
print(user_2.id)
