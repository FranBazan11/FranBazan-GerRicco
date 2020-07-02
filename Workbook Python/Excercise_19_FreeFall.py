print('Calculo de vf en caida libre al tocar el suelo')

g=9.8
Vi=0
Const1=2
h=int(input('Altura inicial (m): '))
if h>0:
	Vf=((Vi**2)+(Const1*g*h))**(1/2)
	print('Velocidad final (Vf) = '+str(round(Vf,2))+'m/s')
else:
	print('Valor introducido incorrecto')