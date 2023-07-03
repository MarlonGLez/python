## Dictionaries ## 

my_dict = dict ()
my_other_dict = {}

print (type(my_dict))
print (type(my_other_dict))

my_other_dict = {"nombre":"Marlon", "Apellido":"Gonzalez", "Edad":31, 1:"Python"}

my_dict = {"nombre":"Marlon", 
           "Apellido":"Gonzalez", 
           "Edad":31, 
           "Lenguajes":{"Python","Swif","Kotlin"}}

print(my_dict)
print(my_other_dict)

print(len(my_dict)) # te dice la cantidad de claves que tiene un diccionario

print(my_dict["nombre"])

my_dict["nombre"] = "ALberto"
print(my_dict["nombre"])

my_dict["Calle"] = "calle 20"
print(my_dict)

del my_dict["Calle"] 
print(my_dict)
 
print("Marlon" in my_dict) # asi se busca x clave
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["nombre", 1, "Piso"]

my_new_dic = my_dict.fromkeys (("nombre", 1)) #crea un diccionario nuevo con los valores nulos
print(my_dict.fromkeys(("nombre", 1)))
 
my_new_dic = dict.fromkeys((my_list))
print(my_new_dic)

my_new_dic = dict.fromkeys(my_dict)
print(my_new_dic)

my_new_dic = dict.fromkeys(my_dict, ("Marlon")) #crea un diccionario con claves de otro diccionario y con datos el valor q pasamos para todos sus valores

print(my_new_dic)




