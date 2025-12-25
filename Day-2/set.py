#create a set
set1={1,2,3,4,4}
print(set1)
#we can't crete a empty set as set1={},bcoz it will treat it as dictionary instead do set1=set()

#update a element in set or insert at a position
#since set isn't ordered we cant update or insert through indexing

#add items to a set
set1.add(15)
print(set1)

#remove a element from set
set1.discard(15)
print(set1)

#set operations
set2={3,4,5,6}
#union of set
print(set1 | set2)

#intersection of sets
print(set1 & set2)

#difference of sets
print(set1 - set2)

#set_symmetry of sets
print(set1 ^ set2)

#check two sets are equal
print(set1 == set2)