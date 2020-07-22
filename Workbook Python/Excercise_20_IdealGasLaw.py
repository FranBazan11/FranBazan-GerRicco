print('Este programa calcula la cantidad de gas en moles')
print('Utilizando: P.V = n.R.T')
R=8.314
C_To_K=273.15
L_TO_M3=1/1000
print('Reyene los datos')
P=float(input('Presion (en Pascales): '))
V=float(input('Volumen (en Litros): '))
T=float(input('Temperatura (en Celcius): '))

#Hago los Calculos
TempEnK=T+C_To_K
V_EnM3=(V*L_TO_M3)
n=((P*V)/(R*T))

print('n = '+ str(round(n,1))+ '(mol/es)')