## Listas ##

my_list = list()
my_other_list = []

print (len(my_list))

my_list = [35, 24, 62, 52, 30, 17]

print (my_list)
print (len(my_list))
my_other_list = [35, 1.77, "Brais", "moure"]
print(my_other_list[0]) 

print (my_list+my_other_list) ## concatenar listas

my_other_list.append("marlonglez") #al final de la lista
print(my_other_list) 

## inserta en una posicion
my_other_list.insert(1, "blue")
print(my_other_list) 

my_other_list.remove("blue") #solo borra el primer elemento con el mismo valor
print(my_other_list) 

my_list.pop()
print(my_list)