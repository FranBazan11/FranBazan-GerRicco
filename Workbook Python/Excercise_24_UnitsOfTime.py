print('Programa para pasar todo a segundos ')

#Establezco las constantes
diasAhoras=24
horasAminutos=60
minutosAsegundos=60

#Pido los datos
print('Reyene los siguientes datos')
dias=int(input('Dias: '))
horas=int(input('Horas: '))
minutos=int(input('Minutos: '))
segundos=int(input('segundos: '))

#Computo de datos
horas1=horas+(dias*diasAhoras)
minutos1=minutos+(horas1*horasAminutos)
segundos1=segundos+(minutos1*minutosAsegundos)

#Imprimo
print('En total son: '+str(segundos1)+' segundos')