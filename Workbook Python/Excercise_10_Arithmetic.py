#Pido datos al usuario
a=int(input('Elegi un numero entero (a) '))
b=int(input('Elegi otro numero entero (b) '))

#Hago todas los computos
suma= a+b
resta= a-b
producto= a*b
cociente= a/b
resto_cociente= a%b #calculo del resto en una division
potencia= a**b

#imprimo todo en pantalla
print('La suma entre a y b es: '+ str(suma))
print('La resta entre a y b es: '+ str(resta))
print('El producto entre a y b es: '+ str(producto))
print('El cociente entre a y b es: '+ str(cociente))
print('El resto del cociente entre a y b es: '+ str(resto_cociente))
print('La potencia de a elevado a b es: '+ str(potencia))