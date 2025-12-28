def save_user(username):
    if not username.strip():
        raise ValueError("Username cannot be empty")
    try:
        with open("Day-5/users.txt",'a',encoding='UTF-8') as user:
            user.write(username +"\n")
    except OSError as e:
        print("file error occured",e)
    else:
        print("username saved successfully")

username=input("Enter username: ")
save_user(username)