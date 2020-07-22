#Declaro todas mis constantes de conversion
piesApulg=12
piesAyardas=(1/3)
piesAmillas=(1/5280)
print('En este programa se convierte de pies a pulgadas, yardas y millas')
#Pido datos al usuario
pies=int(input('Que valor queres convertir? '))
#Hago los computos
pulgadas=(pies*piesApulg)
yardas=(pies*piesAyardas)
millas=(pies*piesAmillas)
#Imprimo en pantalla el resultado
print(str(pies)+'pies es igual a:')
print(str(round(pulgadas,2))+' pulgadas')
print(str(round(yardas,2))+' yardas')
print(str(round(millas,2))+' millas')

