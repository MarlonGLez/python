name, surname, age="Marlon", "GOnzalez",30
print ("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #formato estandart para poder cambiar el idioma de manera facil
print ("Mi nombre es %s %s  y mi edad es %d" %(name, surname, age)) #otra manera de hacerlo %s me asegura q es cadena %d me asegura que sea entero
print (f"Mi nombre es {name} {surname} y mi edad es {age}")  

#Desempaquetado de caracteres
language= "Python"
a, b, c, d, e, f= language 
print(a)
print(b)

#division de un string 

language_slice = language [1:3]
print(language_slice)

language_slice= language[1:]
print(language_slice)

#reverse
reversed_language= language[::-1]
print(reversed_language)

#funciones

print(language.capitalize()) # ka primera mayusc
print(language.upper()) # todas mayusculas
print(language.count("t")) # cantidada de caracteres iguales
print(language.isnumeric()) # me dice si es un numero
print(language.lower()) # minusculas
print(language.upper().isupper()) # devuelve si es upper    
print(language.startswith("Py")) # me devuelve si empieza con la frase 
