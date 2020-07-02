monedas=[200,100,25,10,5,1]

vuelto=int(input('Cuanto es el vuelto que hay que devolver en centavos? '))

for i in range(len(monedas)):
	if (vuelto/monedas[i])>=1:
		cambioA=int(vuelto/monedas[i])
		vuelto=vuelto%monedas[i]
		print('Seran '+ str(cambioA)+' monedas de '+ str(monedas[i])+' centavos de dolar')