#Check Membership Efficiently

def check_membership(list,value):
    if len(list)<=0:
        return False
    set1=set(list)
    return (value in set1)

print(check_membership(["user1", "user2", "user3"],"user4"))
print(check_membership(["user1", "user2", "user3"],"user2"))
