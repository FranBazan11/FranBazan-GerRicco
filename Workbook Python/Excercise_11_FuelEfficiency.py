CONVERTIDOR=235.21
#Pido datos al usuario
eficienciaUS=int(input("Cual es la eficiencia de tu vehiculo en MPG? "))
#Hago el computo
eficienciaCanada=CONVERTIDOR/eficienciaUS
#Imprimo en pantalla el resultado
print("La eficiencia en Litros cada 100km es de: "+ str(eficienciaCanada))