
# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
#cada impresión), sustituyendo los siguientes:
#- Múltiplos de 3 por la palabra "fizz".
#- Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

def fizzbuzz():
 for i in  range(1,101):
    if i%3 == 0 and i%5 !=0 :
       salida="fizz"
    else:
        salida=i
    if i%5 == 0 and i%3 !=0:
        salida="buzz"
    if i%5 == 0 and i%3 ==0:
        salida="fizzbuzz" 
    print(salida)
    
fizzbuzz()
"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS 
     las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.

"""
def is_anagram(palabra_1,palabra_2):
    if palabra_1.lower() == palabra_2.lower():
       return False
    return sorted(palabra_1.lower()) == sorted(palabra_2.lower())

print(is_anagram("Amor", "Roma"))

""" LA SUCESIÓN DE FIBONACCI
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""
def fibonaci_sucec():
    numero_ant=0
    numero_ant2=1
    for i in range(0,50):
        print (numero_ant) 
        fib=numero_ant+numero_ant2
        numero_ant= numero_ant2
        numero_ant2=fib
fibonaci_sucec()
"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""
def is_primo():
    for number in range(1,101):
        if number >= 2:
            tiene_primos=False
            for primo in range(2,number):
                if number % primo == 0:
                    tiene_primos=True
                    break
            if not tiene_primos:
                 print(f"{number}""  ""Es Primo")
is_primo()

"""
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
"""

def invertir_cadenas(cadena):
    reversed_text=""
    tex_len= len(cadena)
    len(cadena)
    for index in range(0,len(cadena)):
        reversed_text+= cadena[tex_len - index -1]
    
    return reversed_text

print(invertir_cadenas("Hola Mundo"))