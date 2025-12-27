from user import User 

user1=User("maruti","maruti@gmail.com")
print(user1.get_profile())
user1.deactivate()
print(user1.get_profile())