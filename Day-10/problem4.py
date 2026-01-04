#Problem 4 (Primary Key Index)

def build_user_index(users):
    index ={}
    for user in users:
        index[user["id"]]=user
    return index
#Why DB indexes exist
# -> bcoz the make the lookup efficient which increases the read speed of a database 

#Why list scanning is slow
# ->bcoz to find a element we need to traverse the entire list which takes O(n) time so it is slow