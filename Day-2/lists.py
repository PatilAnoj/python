#normal list
arr=[1,2,3,4,5,6]
print(arr)

#list of different data types
diff_list=[1,"hello",3,[2,3]]
print(diff_list)

#access item in a list
print(diff_list[1])

#appending a item into list
diff_list.append("new element")
print(diff_list)

#insert at specific position
diff_list.insert(2,"using insert")
print(diff_list)

#add list to existing list
diff_list.extend(arr)
print(diff_list)

#update a element at a position
diff_list[2]="updated item"
print(diff_list)

#remove "new element" from list
diff_list.remove('new element')
print(diff_list)

#remove multiple items from list
del diff_list[1] #delets element at position 1 in list
print(diff_list)

#remove multiple items
del diff_list[0:2]
print(diff_list)
