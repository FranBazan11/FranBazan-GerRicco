print('Programa para pasar de pies y pulgadas a cm')

cambioPiePulg=12
cambioPulgCm=2.54
pies=int(input('Cuantos pies medis? '))
pulgadas=int(input('Y cuantas pulgadas? '))

TotalPulgadas= pulgadas+(pies*cambioPiePulg)
Totalcm=(TotalPulgadas*cambioPulgCm)

print('Es decir que medis '+ str(Totalcm)+'cm. ')