-python is dynamically typed interpreted language
-variables are not required to specify their types
-python consists of basic data types like int,float,string,boolean
-virtual environment creates a environment for a project that stores the versions of the libraries used for that specific project
-we use input() to take inputs from user ,and input() returns string by default
-type() is used to get the type of a variable 

#DAY-2

LISTS
-Lists in python are same as dynamic arrays that can store data of different data types
-Lists in python are ordered,i.e they maintain order of items
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

#DAY-3

FUNCTIONS
-function is a block of code that performs specific task
-functions are created using def keyword
def function_name():
    print("hello this is function")

-we can pass parameters to a function while it's declaration inside the brackets i.e def function_name(param1,param2,....)
-the value of the parameters is passed while calling the function(argument1,argument2,...) this is called argument
-we can pass default values of parameters if no argument is passed, while declaring the function using def person2(name="jay",age=18,course="java"):
-Using *args allows a function to take any number of positional arguments.
-using **kwargs allows a function to accept any number of keyword arguments.

SCOPE
-a variable scope specifies where a varible can be accessed 
-there are 3 types of scopes local,global,nonlocal

NON-LOCAL
-In Python, the nonlocal keyword is used within nested functions to indicate that a variable is not local to the inner function, but rather belongs to an enclosing function’s scope.

#DAY-4

CLASSES
-class is considered as blueprint of objects 
-

SELF
-it is a convention based paramater used in class to refer to the current instance (OBJECT) of that class
-SELF is not a reserved keyword we can use any name for the first parameter of the class method,but self is used as industry standard 

Why __init__ runs automatically
-The __init__ method (short for "initialization") runs automatically because it is a special "dunder" (double-underscore) method that Python's object creation process is programmed to call whenever a new instance (object) of a class is created. 
-__init__ is the constructor of the class,it is initialised at the time of object creation,used to initialise the values of the variables in the class

instance variables are unique to each object and store data specific to that instance, while class variables are shared by all instances of a class and store common attributes or default settings. 

#DAY-5

EXCEPTION
-exception in python are error at runtime (not invalid syntax error)
-we can handle it using try except block
-if an exception occurs in try the except block executes
-else is also used with try except
-else executes only when the try block runs without any exception
-finally is executed every time irrespective of exception

FILES 
-to open a file we use open("file_path") function
-once a file is opened it is strictly the developer's responsibility to close it
-the file that is opened must be closed
-to do that automatically python provided with statement
with open("file_path") as f:

Why with is better than open/close
-because The with statement automatically takes care of closing the file once it leaves the with block, even in cases of error. I highly recommend that you use the with statement as much as possible, as it allows for cleaner code and makes handling any unexpected errors easier for you.

-to write in a file
with open("file_path",'w') as writer:
    writer.write()

-to read a file
with open("file_path",'r')as reader:
    reader.read()


Q.why sql operates on sets instead of loops?
->SQL is declarative and operates on sets because databases are optimized to process large volumes of data using query planners and indexes, avoiding row-by-row iteration in application code.

Q.Why DB constraints are still required even if backend validates?
->DB constraints protect data integrity even if backend logic fails, bugs are introduced, or multiple services write to the same database.

