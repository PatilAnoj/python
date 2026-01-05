#DELETE with WHERE (Even More Dangerous)

def delete_user(users, user_id):
    for user in users:
        if user_id == user["id"]:
            users.remove(user)
            return True
    return False
#Why is DELETE without WHERE catastrophic?
# ->coz, delete without where condition deletes the entire table which can lead to huge loss,
#   the where condition tells us to delete the particular matching row instead of whole table 