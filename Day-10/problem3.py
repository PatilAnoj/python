#Data Integrity Guard

def validate_user(users, user):
    if user["id"]<0:
        raise ValueError("invalid id")
    if not user["username"].islower() or not (3<=len(user["username"])<=15):
        raise ValueError("invalid username")
    
    if not "@" in user["email"]:
        raise ValueError("invalid email")
    
    for user1 in users:
        if user["username"].lower()==user1["username"].lower() or user["email"]==user1["email"]:
            raise ValueError("email or username already exists")
        
    return True
