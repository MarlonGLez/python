### File Handling ###
import os
txt_file= open("intermediate/my_file.txt", "r+") 
#print(txt_file.read())
#print(txt_file.read(10)) # lee cantidad de caracteres
#print(txt_file.readline()) # line a linea
#print(txt_file.readlines()) #cada linea lo convierte en un elemento de una lista
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambin kotlin")