print('Este programa calcula la energia que debe ser suministrada o quitada')
print('para llevar una masa de agua a la temperatura deseada')
#DECLARO CONSTANTES
Cagua=4.186 #C: ES LA CAPACIDAD CALORIFICA
costo=8.9
ConversionA=(1/3600000)
#PIDO DATOS AL USUARIO
print('Complete los datos necesario en mililitros y en grados celisius')

m=int(input('Masa: '))
Tinicial=float(input('Temperatura inicial: '))
Tfinal=float(input('Temperatura final(deseada): '))

#HAGO LOS CALUCLOS
diferenciaTemp=Tfinal-Tinicial
q= m*Cagua*diferenciaTemp #q: energia necesaria
q_kwh=q*ConversionA
CostoFinal=q_kwh*costo

#IMPRIMO EN PANTALLA
if q>0:
	print('q = '+str(round(q,2))+' es decir que se le deben aportar '+str(round(q,2))+' Joules')
	print('Y esta energia te cuesta '+str(round(CostoFinal,1))+' centavos')
elif q<0:
	print('q = '+str(round(q,2)*(-1))+' es decir que se le deben remover '+str(round(q,2)*(-1))+' Joules')
	print('Y esta energia te cuesta '+str(round(CostoFinal,1)*(-1))+' centavos')
else:
	print('La temperatura final (deseada) es la actual asique esta todo joya')