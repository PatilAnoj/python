#UPDATE with WHERE (Danger Zone)

def update_user_age(users, user_id, new_age):
    if new_age<18:
        raise ValueError("invalid age must be 18 or above")
    
    for user in users:
        if user_id == user["id"]:
            user["age"]=new_age
            return users
    raise ValueError("user doesn't exists")

#What happens in SQL if you forget the WHERE clause?
# -> it will update the age of all records present in table to new_age
