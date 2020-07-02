import time  #El modulo time te permite trabajar con la fecha actual
tiempoSegundos = time.time()  #fecha en segundos desde no se que dia
print(str(tiempoSegundos)+'\n')
tiempoCadena = time.ctime(tiempoSegundos) #pasar esa fecha en segundos a normal
print(tiempoCadena)
