print("Programa de libreta")
notas_matematica=int(input("Cuantas notas tenes en matematicas? "))
matematicas=[]
suma=0

#bucle que analiza las notas
while len(matematicas) < notas_matematica:
	matematicas.insert(int(len(matematicas)),input("inserte la "+ str(1+int(len(matematicas))) + " nota de matematica: "))
#for para iterar en toda la suma
for i in range(int(len(matematicas))):
	suma = suma + int(matematicas[i])

promedio= round(suma/len(matematicas),2)
print("tu promedio en matematicas es: " + str(promedio))
