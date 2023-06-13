## Sets ## 

my_set = set()
my_other_set = {} #Inicialmente es un diccionario

my_other_set = {"marlon", "Gonzalez", 30}
print(type(my_other_set))

print(len(my_other_set)) 

my_other_set.add("blackstar")
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("blackstar") # un set no admite repetidos  
print(my_other_set) 

print("marlon" in my_other_set) #para saber si esta en el set
my_other_set.remove("marlon")
print(my_other_set) 

my_other_set

my_other_set.clear()
print(my_other_set)