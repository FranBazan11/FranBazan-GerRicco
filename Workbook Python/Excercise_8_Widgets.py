peso_widget=75
peso_gizmo=112
#pido datos al usuario
cantidad_widget=int(input('Cuantos widgets vas a querer? '))
cantidad_gizmo=int(input('Cuantos gizmos vas a querer? '))
#Hago los calculos del peso
peso_total=(cantidad_widget*peso_widget)+(cantidad_gizmo*peso_gizmo)
#Imprimo en pantalla
print('El peso total del pedido es de '+ str(peso_total)+'g.')