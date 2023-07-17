
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