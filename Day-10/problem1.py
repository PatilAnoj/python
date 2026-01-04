#In-Memory User Table (CRUD)

def create_user(users,new_user):
    for user in users:
        if new_user["id"] == user["id"]:
            raise ValueError("id already exists")
    
    users.append(new_user)
    return users


def get_user_by_id(users, user_id):
    for user in users:
        if user_id == user["id"]:
            return user
        
    return None

def update_user_email(users, user_id, new_email):
    for user in users:
        if  user_id == user["id"]:
            user["email"]=new_email
            return users
    raise ValueError("user_id not found")

def delete_user(users, user_id):
    for user in users:
        if user["id"]== user_id:
            users.remove(user)
            return True
    return False

users=[]
print(create_user(users,{
  "id": 1,
  "username": "john",
  "email": "john@gmail.com"
}))
print(create_user(users,{
  "id": 2,
  "username": "johnanna",
  "email": "johnanna@gmail.com"
}))
        