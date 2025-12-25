#create a dictionary
new_dict={
    "name":"krrish",
    "age":23,
    "is_male":True
}

print(new_dict)

#access items in dictionary
print(new_dict["name"])

#add new item in dictionary
new_dict["father name"]="rakesh"
print(new_dict)

#delete item in dictionary
del new_dict["father name"] #we can also use pop() to delete 
print(new_dict)

#update element in dictionary
new_dict["age"]=33
print(new_dict)

#merge two dictionaries
dict2={
    "name2":"krrish2",
    "age":23,
    "is_male":False
}

merged_dict=new_dict | dict2
print(merged_dict)

