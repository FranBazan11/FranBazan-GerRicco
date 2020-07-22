print('Calculo del volumen del cilindro')
import math
#Declaro constantes
pi=math.pi
expo1=2
#Pido datos
print('Coloca todos los datos necesarios en metros')
radio=float(input('Radio: '))
altura=float(input('Altura: '))
#Hago los calculos
area=pi*(radio**expo1)
volumen=area*altura
#Imprimo en pantalla
print('Volumen = '+ str((round(volumen,1)))+' metros cubicos')