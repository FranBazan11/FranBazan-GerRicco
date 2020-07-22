interes_por_agno=0.04
#Pido datos al usuario
Depositado=float(input('Cuanto dinero tenes depositado en la cuenta de ahorros? '))
#Hago el computo
agno=0
while agno <3:
	Depositado=Depositado+(Depositado*interes_por_agno)
	agno=agno+1
	print('el ' + str(agno) + 'agno tenes ' + str(round(Depositado,2))+ ' depositados en la cuenta de ahorros')
print('fin')

#Use el comando predefinido round() para redondear a 2 dijitos despues de la coma
