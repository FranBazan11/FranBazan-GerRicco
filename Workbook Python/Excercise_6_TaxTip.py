Tasa_impuesto=0.21
Tasa_propina=0.18

#Pido datos al usuario
costo=float(input('Cuanto costo la comida en el restaurante? '))

#Calculos necesarios
propina= costo*Tasa_propina
impuesto= costo*Tasa_impuesto
costoFinal= costo+propina+impuesto
#Imprimo en pantalla
print('El impuesto es de: ' + str(impuesto))
print('De propina se dara:' + str(propina))
print('Por lo que en total debera gastar: ' + str(costoFinal))