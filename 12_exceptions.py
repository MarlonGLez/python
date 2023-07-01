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
else:
    print("La ejecucion continua correctamente")
finally:
    print("La ejecucion continua ")