#INSERT with Constraints (DB Enforcement)

def insert_user(users, new_user):
    if not (isinstance(new_user["id"],int)) or (new_user["id"]<=0):
        raise ValueError("invalid id ")
    if not (new_user["username"].islower()) or not (3<=len(new_user["username"])<=15):
        raise ValueError('invalid username')
    
    if not (isinstance(new_user['age'],int)) or  (new_user['age']<18):
        raise ValueError("invalid age")
    for user in users:
        if  new_user["id"] == user["id"] :
            raise ValueError("id already exists")
        if new_user["username"] == user["username"]:
            raise ValueError('username already exists')
    users.append(new_user)
    return users

            
        
    
        