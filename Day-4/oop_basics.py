#class definition

class basic:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display_info(self):
        print(self.name,"is",self.age,"years old")
obj1=basic("john",24)
obj1.display_info()

obj2=basic("jazz",23)
obj2.display_info()