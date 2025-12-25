#Remove duplicates from list

list1=[1,2,2,3,4,4,4,5]
list1=list(set(list1))
print(list1)

#count word frequency in string
str="I love python and I love backend python"
str=str.split(' ')
dict={}
for word in str:
    if(word in dict):
        dict[word]=dict[word]+1
    else:
        dict[word]=1

print(dict)

#find maximum and minimum in list

list3=[45, 12, 89, 33, 2, 67]
max=list3[0]
min=list3[0]

for elem in list3:
    if(elem>max):
        max=elem
    if(elem<min):
        min=elem

print("max ",max)
print("min ",min)

#merge two dictionaries

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 40}

for elem in dict1:
    if(elem in dict2):
        dict1[elem]=dict1[elem] + dict2[elem]

for elem in dict2:
    if(elem not in dict1):
        dict1[elem]=dict2[elem]

print(dict1)