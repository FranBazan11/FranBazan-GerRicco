#PROYECTO PARA CALCULAR QUE ME CONVIENE VENDER EN ALBION ONLINE

#Establezco algunas cositas
totalfibras=['t2','t3','t4','t4.1','t4.2','t4.3','t5','t5.1','t5.2','t5.3','t6','t6.1','t6.2','t6.3','t7','t7.1','t7.2','t7.3','t8','t8.1','t8.2','t8.3']

mis_fibras=[]
cant_a=[]              #a son fibras ; b son telas ; c son Tunicas
valor_a=[]
valor_b=[]
valor_c=[]

#Pido algunos datos
print('Recordando que:\n t2 = Algodon\n t3 = Lino\n t4 = Cañamo\n t5 = Duranta\n t6 = Algodon Rojo\n t7 = Lino Solar\n t8 = Cañamo Fantasma\n')
print(totalfibras)

cant_fibras= int(input('Cuantos tipos de fibra tenes para usar? '))

for i in range(cant_fibras):
	mis_fibras.append(str(input('de la lista, que fibra tenes? ')))
	cant_a.append(int(input('Cuantas fibras '+ str(mis_fibras[i]) + ' tenes?')))
	valor_a.append(int(input('Cuanto vale en promedio la fibra? ')))
	valor_b.append(int(input('Cuanto vale en promedio la tela')))
	valor_c.append(int(input('Cuanto vale en promedio la tunica?')))

#Hago unas cuenticas



#FALTA
#QUE SE FIJE QUE COSAS ES POSIBLE FABRICAR CON LO QUE TENGO Y QUE PROMEDIE CUANTO GANARIA, Y QUE ME CONVIENE HACER
#ACORDARSE DE AGREGAR LA POSIBILIDAD DE TRANSMUTACION
#FIJARSE COMO CONVIENE ALMACENAR LAS CONSTANTES PARA LOS CALCULOS
