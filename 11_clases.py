 ## Clases ##
 
class Person:
    def __init__(self, name, surname, alias="Sin Alias"):
        self.fullname = f"{name} {surname}" #publica
        self.__name= name #privada
    
    def getname(self):
        return self.__name

my_person = Person("Marlon", "Gonzalez")
print (f"{my_person.getname()}")