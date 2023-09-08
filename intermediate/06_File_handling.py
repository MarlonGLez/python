### File Handling ###
import os
txt_file= open("intermediate/my_file.txt", "w+") 
txt_file.write("Mi nombre es marlo\nMi apellido gonzalwz\n35 años\nLenguage preferido python")
#print(txt_file.read())
#print(txt_file.read(10)) # lee cantidad de caracteres
#print(txt_file.readline()) # line a linea
#print(txt_file.readlines()) #cada linea lo convierte en un elemento de una lista
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambin kotlin")
print(txt_file.readline())

txt_file.close()
#os.remove("intermediate/my_file.txt")

#.josn file

import json

json_file = open("intermediate/my_file.json","w+")
json_text = {"Name":"Marlon",
             "Surname":"Gonzalez",
             "Age":31,
             "Language":"Python"}
json.dump()