conversiones=[86400, 3600, 60, 1]
cosas=['dias','horas','minutos','segundos']
lista=[]

segundos=int(input('Segundos: '))

for i in range(4):
	if (segundos/conversiones[i])>=1:
		lista.insert(i,((segundos//conversiones[i])))
		segundos=segundos%conversiones[i]
	else:
		lista.insert(i,0.0)
	#IMPRIMO TODO EN PANTALLA
	print(cosas[i] +' = ' + str(lista[i]))