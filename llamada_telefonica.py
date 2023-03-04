# conocer el costo de una llamada segun la duracion de la misma 

print("---------------------------------")
print("------costo de la llamada--------")
print("---------------------------------")

# input
dl = int(input("Digite la duracion de la llamada: "))

# procesing

if dl <= 3:
    cl = "300"
else:
    m = dl - 3
    cl = 300+(50*m)

# output
print("El costo de la llamada es: "+str(cl))

