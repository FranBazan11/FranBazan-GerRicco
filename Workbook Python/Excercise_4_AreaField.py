#pido datos al usuario
largo=float(input('cuantos pues de largo tiene el campo? '))
ancho=float(input('y de ancho? '))

#hago  el calculo (1 acre=43560pies)
area_pies= largo*ancho
area_acre= area_pies*(1/43560)

#imprimo el resultado
print('el area del campo en acre es de: ' + str(area_acre))