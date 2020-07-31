#Constantes (Algunas no son tan constantes)

TaxPremium = 0.02   #2% (averiguar si sigue siendo esta cuando te hagas premium)
TaxNormal = 0.06    #6%
AjusteCuota = 0.015 #1,5%

def CalculosVenta(CantidadFibra,PrecioFibra):
	GananciaBruta = CantidadFibra*PrecioFibra
	Impuesto = GananciaBruta*TaxNormal
	SetupFee = GananciaBruta*AjusteCuota
	Ganancia = GananciaBruta-Impuesto-SetupFee
	print('La ganancia bruta es de: '+ str(GananciaBruta)+' de plata')
	print('Restandole impuestos y coste queda en '+ str(Ganancia)+' de plata')

#Entrada de Datos
CantFibra = int(input('Cuanta fibra recolectaste? '))
PrecioFibra = int(input('A cuanto se vende cada fibra? '))

#Calculos de Venta
CalculosVenta(CantFibra,PrecioFibra)