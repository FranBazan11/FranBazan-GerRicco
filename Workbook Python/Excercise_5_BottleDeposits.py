#pido datos al usuario
botellasChicas=int(input('Cuantas botellas de 1 litro o menos tenes? '))
botellasGrandes=int(input('Cuantas botellas de mas de 1 litro? '))

#Hago los calculos
deposito= ((0.10 * (botellasChicas)) + (0.25 * (botellasGrandes)))

#imprimo en pantalla
print('por tus botellas se te dara un recompensacion de ' + str(deposito)+ '$')
