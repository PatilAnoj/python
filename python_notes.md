-python is dynamically typed interpreted language
-variables are not required to specify their types
-python consists of basic data types like int,float,string,boolean
-virtual environment creates a environment for a project that stores the versions of the libraries used for that specific project
-we use input() to take inputs from user ,and input() returns string by default
-type() is used to get the type of a variable 

#DAY-2

LISTS
-Lists in python are same as dynamic arrays that can store data of different data types
-Lists in python are ordered,i.e the maintain order of items
-they are mutable,i.e items in list once created can be changed later
-list can store different values
-we use list_name.append(element to insert) to insert new item in list at the last position.
-to insert at specific position in list we use insert(position,element)
-to add existing list to a list we use extends() function
-to update list[position]=element
-to remove a item from list list.remove(item)
-we can also use del to remove items from list
-del list[start:end] is used to delete elements in that range at once.

TUPLES
-Tuples also maintain the order of elements
-Tuples are immutable,i.e they cannot be changed after creation
-Tuples can contain duplicte values
-we cannot insert,update or delete elements in tuple it will throw a error 

DICTIONARY
-dictionary is same as list and tuples but contains each element as key:value pair
-the keys in dictionary should be immutable data type such as integer,string,tuple,etc...
-dictionaries don't maintain order
-dictionaries are mutable
-dictionaries don't allow duplicate keys

SETS
-sets are not ordered
-sets don't allow duplicates
-since set isn't ordered we cant update or insert through indexing
-set can have many number of elements of different data types,but set cannot have mutable data types like lists,sets,dictionary as its element
#set operations
- |,union() => union =>prints all elements from set A and set B
- &,intersection() => intersection => prints common elements from set A and set B
- -,difference() => difference => prints elements of set A that are not in set B
- ^,symmetric_difference() => symmetric difference => prints all elements from set A and set B except the common elements
- ==  => used to check if two sets are equal or not i.e both sets contains same elements