#User Registration Validation
def check_data_presence(user):
    if "username" not in user:
        raise ValueError("Missing username") 
    if "email" not in user:
        raise ValueError("Missing Email") 
    if "age" not in user:
        raise ValueError("Missing age") 
    return True

def check_data_type(user):
    if not isinstance(user["username"],str):
        raise ValueError("username must be string") 
    if not isinstance(user["email"],str):
        raise ValueError("email must be string") 
    if not isinstance(user["age"],int):
        raise ValueError("age must be number") 
    return True

def check_format(user):
    if not user["username"].islower():
        raise ValueError("username must be in lowercase") 
    if not "@" in user["email"]:
        raise ValueError("Invalid email format") 
    return True

def check_range(user):
    if not 3<=len(user["username"])<=15:
        raise ValueError("Invalid length of username") 
    if not 18<=user["age"]<=60:
        raise ValueError("Invalid age") 
    return True

def user_reg_validation(user):
    if check_data_presence(user) and check_data_type(user) and check_format(user) and check_range(user):
        return "VALID"
    

print(user_reg_validation({
  "username": "string",
  "email": "string@gmail.com",
  "age": 19
}))

