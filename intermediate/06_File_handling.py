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
             "Languages":["Python", "Swift" ,"Code"]}
json.dump(json_text,json_file, indent = 2)

json_file.close()

with open("intermediate/my_file.json") as my_other_file: 
    for line in my_other_file.readlines():
      print (line)

json_dict = json.load(open("intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["Name"])

#.csv file
import csv
csv_file = open("intermediate/my_file.csv","w+")
csv_writer= csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language"])
csv_writer.writerow(["Marlon", "Gonzalez", 31, "Python"])

csv_file.close()

with open("intermediate/my_file.csv") as my_other:
    for line in my_other.readlines():
        print(line)

#.xlsx file
#hay q instalar el modulo

#.xlm file
import xml