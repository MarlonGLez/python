## Tuples ## son inmutables

my_tuple = tuple()
my_other_tuple = ()

my_tuple  = (35, 177 , "Marlon", "gonzalez")
my_other_tuple = (1,3,4,5,6)
print(my_tuple)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple.index(177)) #indice del primer elemento 

my_sume_tuple = my_other_tuple + my_tuple
print(my_sume_tuple)