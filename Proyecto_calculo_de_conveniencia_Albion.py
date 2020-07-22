#CONSTANTES Y OTRAS COSAS QUE USO DESPUES

Fibras=['T2','T3','T4','T4.1','T4.2','T4.3','T5','T5.1','T5.2','T5.3','T6','T6.1','T6.2','T6.3']
contador1=0
totalBruto=0
misFibras=[]
cantidadesDeFibras=[]
costoFibras=[]

#INFO

print(Fibras)
CantidadFibras=int(input('De la lista, Cuantos tipos de Fibra tenes ? '))
if CantidadFibras <= len(Fibras):
	while contador1 < CantidadFibras:
		seleccion=str(input('Cual tenes? '))
		if seleccion in Fibras:
			misFibras.insert(contador1, seleccion)
			cantidadesDeFibras.insert(contador1, int(input('Cuantas fibras ' + str(seleccion) + ' tenes? ')))
			costos.insert(contador1, int(input('A cuanto vendes cada fibra ' + str(seleccion) + ' ? ')))
			contador1=contador1 + 1
		else:
			print('Escribiste mal, volve a intentarlo')
else:
	print('no existen tantos tipos')

#CALCULOS

for i in range(len(costoFibras)):
	totalBruto = totalBruto + (cantidadesDeFibras[i]*costoFibras[i])  #Calculo de si vendo todo como fibras
print(totalBruto)

#TENGO QUE BUSCAR LA FORMA DE HACER UN CALCULO PARA QUE ENCUENTRE LA FORMA MAS RENTABLE DE TODAS DE VENDER MIS PRODUCTOS
#FIJARME PORCENTAJE DE DEVOLUCION DE MATERIALES AL FABRICAR TELAS Y ATUENTOS
#NO SER TAN PAJERO Y HACER FUNCIONES, Y ME PARECE QUE HAY COSAS QUE MEJOR ALMACENAR EN CLASES
#PENSAR SI TAMBIEN PUEDO LLEGAR A TENER EN CUENTA CON LOS PORCENTAJES DE APARICION DE MATERIALES QUE ME CONVIENE HACER, O LA VELOCIDAD DE RECOLECTAR

