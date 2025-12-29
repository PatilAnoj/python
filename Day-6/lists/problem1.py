#Remove duplicates from lists
def remove_duplicates(input):
    if len(input)<=1 :
        return input
    list1=[]
    for username in input:
        if username not in list1:
            list1.append(username)
    return list1

print(remove_duplicates(["a", "b", "a", "c", "b"]))