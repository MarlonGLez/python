 ## Exception handling ##
 
numberone = 5
numbertwo = 1
numberthre = "2"

try:
    print(numberone + numberthre)
    print("No se ha producido error")
except:
    print("Se ha Producido un error")
    
try:
    print(numberone + numberthre )
    print("No se ha producido error")
except:
    print("Se ha Producido un error")
else:#opcional
    print("La ejecucion continua correctamente")
finally: #opcional
    print("La ejecucion continua ") #siempre se ejecuta
try:
    print(numberone + numberthre)
    
    print("No se ha producido error")
except TypeError:
    print("Se ha Producido un error")
    
#captura la informacion de la excepcion
try:
    print(numberone + numberthre)
    print("No se ha producido error")
except ValueError as error: # captar el error
    print(error)
except Exception as exception_error:
    print(exception_error)