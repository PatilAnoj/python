#positional arguments

def person(name,age,course):
    print(name,"is",age,"and is enrolled in",course)
person("john",23,"python")

#default arguments
def person2(name="jay",age=18,course="java"):
    print(name,"is",age,"and is enrolled in",course)
person2()

#*args to take multiple positional arguments

def person3(*scores):
    print(sum(scores))
person3(1,2,3,4,5,6)

#**kwargs to take multiple keyword arguments

def person4(**words):
    for key,value in words.items():
        print({key},":",{value})
person4(name="john",course="cpp")