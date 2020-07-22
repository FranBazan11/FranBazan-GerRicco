#pido datos del usuario
n = int(input('Escriba un numero entero positivo '))
if n > 0:
	#hago el calculo
	suma= ((n)*(n+1))/2
	print('La suma de todos los enteros de 1 a n es: ' + str(suma))
else:
	print('el numero introducido no es valido ')