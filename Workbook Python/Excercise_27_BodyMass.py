#Pido los datos
peso=float(input('Cuanto es tu peso (kilogramos): '))
altura=float(input('Cuanto medis(metros): '))
#Computo
BMI=peso/(altura*peso)
#Imprimo en pantalla
print('Tu indice de masa corporal es: '+str(round(BMI,1)))