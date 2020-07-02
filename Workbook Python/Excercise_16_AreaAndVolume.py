print('Programa para determinar area y volumen dando el radio')
#Declaro mis constantes
import math
pi=math.pi
pot1=2
pot2=3
constB=(4/3)
#Pido datos al usuario
radio=float(input('Determine un valor de radio en centimetros '))
#Hago los calculos
Area=pi*(radio**pot1)
Volumen=(constB*pi*(radio**pot2))
#Imprimo en pantalla
print('Con radio '+str(radio))
print('El Area de la circunferencia es de '+ str(round(Area,2))+'cm. cuadrados')
print('El Volumen de la esfera es de '+ str(round(Volumen,2))+'cm. cubicos')
