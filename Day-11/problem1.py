#Simulate a Table (Users)

def select_all(users):
    return users

def select_where_age_gt(users, age):
    filtered_list=[x for x in users if x['age']>age]
    return filtered_list

def select_by_username(users, username):
    filtered_list=[x for x in users if x['username']==username.lower()]
    return filtered_list

print(select_all([
  {"id": 1, "username": "john", "age": 25},
  {"id": 2, "username": "alice", "age": 30},
  {"id": 3, "username": "bob", "age": 17}
]))