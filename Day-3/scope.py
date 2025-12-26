#global scope variabe
This_is_global="i am global variable"

#variable local scope 
def scope():
    sum=2+3 #variable sum is local scoped to scope function since it is created inside it ,it can't be accessed out of scope() function
    print(sum)
    print(This_is_global)
scope()

print(This_is_global)


#non local scope variable

def outer():
    message="local"
    def inner():
        nonlocal message
        message="nonlocal"
        print("inner",message)
    inner()
    print("outer",message)
outer()

print(__name__)