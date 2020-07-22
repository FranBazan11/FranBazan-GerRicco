print('Programa para devolver el vuelto en la menor cantidad de monedas posibles')

#Empiezo declarando las variables en centavos de dolar
A=1
B=5
C=10
D=25
E=100
F=200
#Le pido el dato a el usuario
vuelto=int((input('Cuantos centavos son de vuelto? ')))

#Hago los computos
if (vuelto/F)>1:
	CambioF=int(vuelto/F)
	vuelto=(vuelto%F)
	print(str(CambioF)+' monedas de 2 dolares')
if (vuelto/E)>1:
	CambioE=int(vuelto/E)
	vuelto=(vuelto%E)
	print(str(CambioE)+' monedas de 1 dolar')
if (vuelto/D)>1:
	CambioD=int(vuelto/D)
	vuelto=(vuelto%D)
	print(str(CambioD)+' monedas de cuarto de dolar')
if (vuelto/C)>1:
	CambioC=int(vuelto/C)
	vuelto=(vuelto%C)
	print(str(CambioC)+' monedas de 10 centavos de dolar')
if (vuelto/B)>1:
	CambioB=int(vuelto/B)
	vuelto=(vuelto%B)
	print(str(CambioB)+' monedas de 5 centavos de dolar')
if (vuelto/A)>=1:
	CambioA=int(vuelto/A)
	vuelto=(vuelto%A)
	print(str(CambioA)+' monedas de 1 centavo de dolar')

print('FIN')