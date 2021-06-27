import random
import matplotlib.pyplot as plt
import numpy as np
from colorama import init, Fore, Back, Style

#2) Replicar los resultados del trabajo “A Markov Chain Model for Covid-19 Survival Analysis”
#A) Seccion 3.0: A More Complex Markov Chain

'''En este caso se consideran 5 estados: 0: Paciente sano. 1: Paciente infectado. 2: Paciente hospitalizado.
3: Paciente en ICU (Cuidados intensivos). 4: Dead (estado absorbente) 
Si el paciente cae en estado Dead, ya no puede salir del mismo, es un estado absorbente.

A su vez se tiene una matriz P donde se modela la matriz de transición de probabilidad de Markov.
Este modelo se considera mas realista y complejo, similar a las situaciones presentadas en Italia o
Nueva York en sus crisis de COVID 19.
'''
#!!!!!!!!!!!!!!!!!!!!!!
#INCLUIR FOTO DEL PAPER DONDE MUESTRA EL DIAGRAMA!!!!!! Y LA MATRIZ P
#!!!!!!!!!!!!!!!!!!!!!!

'''
Este modelo, si no se aplica inmunidad de ningun tipo contra la enfermedad y si se aplican 
suficientes iteraciones de tiempo, invariablemente finalizara con la muerte de toda la población. 

En este caso, como invariablemente los pacientes van a morir, no tiene sentido buscar la solución
en estado estacionario, entonces lo que el paper nos muestra es la probabilidad de morir a largo plazo
y los tiempos esperados para morir, comenzando en los estados 1, 2, 3.
Para ello obtenemos una sub matriz de P, llamada Q, en la que se elimina la fila y columna del estado Dead,
y luego se invierte esta matriz (I-Q)**(-1).'''

#!!!!!!!!!!!!!!!!!!!!!!
#INCLUIR FOTO DEL PAPER DONDE MUESTRA LA MATRIZ INVERTIDA
#!!!!!!!!!!!!!!!!!!!!!!

'''El paper nos presenta una tabla donde se presenta el tiempo promedio hasta la muerte del paciente, partiendo
desde cada uno de los estados posibles.
Luego nos muestra una tabla de probabilidades de que un paciente muera en N dias empezando desde cualquiera
de los estados transitorios. Esto se calcula con la propiedad de Markov. Observamos que la probabilidad de morir
en menos de 16 dias es relativamente baja, siempre y cuando el paciente no entre en ICU.
Luego se calcula la matriz F, obteniendo la probabilidad de que una persona alcance algún estado de la Cadena
de Markov, especialmente el estado absorbente de morir, dado que dicha persona comienza en cualquiera 
de los estados anteriores. La matriz F muestra la importancia de evitar una alta tasa de infección a largo plazo.'''

#!!!!!!!!!!!!!!!!!!!!!!
#INCLUIR FOTO DEL PAPER DONDE MUESTRA LAS TRES TABLAS
#!!!!!!!!!!!!!!!!!!!!!!

''' ARMAMOS LA MATRIZ DE PROBABILIDADES '''
sistema = {"p00" : 0.93, "p01" : 0.07, "p02" : 0, "p03": 0, "p04": 0, 
		   "p10": 0.05 , "p11" : 0.80, "p12" : 0.1,"p13":0.05, "p14":0,
		   "p20": 0, "p21": 0.15, "p22": 0.8,"p23":0.05, "p24":0,
		   "p30": 0, "p31": 0, "p32": 0.05,"p33":0.80, "p34":0.15,
		   "p40": 0, "p41": 0, "p42": 0,"p43":0, "p44":1}

inversa = {
	"q00" : 26.1905, "q01" : 16.6667, "q02" : 10.0000, "q03" : 6.66667,
	"q10" : 11.9048, "q11" : 16.6667, "q12" : 10.0000, "q13" : 6.66667,
	"q20" : 9.5238, "q21" : 13.3333, "q22" : 13.3333, "q23" : 6.66667,
	"q30" : 2.3810, "q31" : 3.3333, "q32" : 3.3333, "q33" : 6.66667
}

def sistema_verificacion(sistema,inversa):
	'''La matriz inversa contiene el número promedio de visitas a cada estado'''
	'''Al ser el estado Dead un estado absorbente nos interesa saber la cantidad
	de dias que se espera que pasen hasta llegar a el, partiendo desde cada uno de los
	estados'''
	'''El tiempo promedio antes de ser infectado es el indicado en la posicion (0,0)
	de la matriz inversa'''
	tinfectado = inversa["q00"]
	print("Tiempo promedio antes de infectarse: " + str(tinfectado) + " dias")

	'''Para obtener el tiempo promedio desde el estado Sano hasta dead sumamos todos
	los elementos de la primera fila'''
	tsanoamorir = inversa["q00"] + inversa["q01"] + inversa["q02"] + inversa["q03"]
	print("Tiempo promedio desde el estado Sano hasta morir: " +
		str(tsanoamorir) + " dias")

	'''De manera analoga calculamos el resto de las posibilidades''' 
	tinfectadoamorir = inversa["q01"] + inversa["q02"] + inversa["q03"]
	print("Tiempo promedio desde el estado Infectado hasta morir: " +
		str(tinfectadoamorir) + " dias")
	thospitalizadoamorir = inversa["q02"] + inversa["q03"]
	print("Tiempo promedio desde el estado Hospitalizado hasta morir: " +
		str(thospitalizadoamorir) + " dias")
	ticuamorir = inversa["q03"]
	print("Tiempo promedio desde el estado ICU hasta morir: " +
		str(ticuamorir) + " dias")
	print("")

	'''Ahora queremos calcular las probabilidades de que un paciente muera empezando en cualquiera
	de los estados, en una cantidad de dias definidos que son 2, 4, 8 y 16'''
	'''Esto se puede calcular con la propiedad de Markov: P**M = P * P * ... * P (M dias) '''

	'''Calculamos la probabilidad de llegar al estado Dead en 2 dias'''
	'''Para ello nos interesa calcular P**2 y mirar los valores de la ultima columna'''
	print("La probabilidad de morir en 2 dias desde estado Sano es: " +
		str(sistema["p00"] * sistema["p03"] + sistema["p01"] * sistema["p14"] 
		+ sistema["p02"] * sistema["p24"] + sistema["p03"] * sistema["p34"]
		+ sistema["p04"] * sistema["p44"]))

	print("La probabilidad de morir en 2 dias desde estado Infectado es: " +
		str(sistema["p10"] * sistema["p03"] + sistema["p11"] * sistema["p14"] 
		+ sistema["p12"] * sistema["p24"] + sistema["p13"] * sistema["p34"]
		+ sistema["p14"] * sistema["p44"]))

	print("La probabilidad de morir en 2 dias desde estado Hospitalizado es: " +
		str(sistema["p20"] * sistema["p03"] + sistema["p21"] * sistema["p14"] 
		+ sistema["p22"] * sistema["p24"] + sistema["p23"] * sistema["p34"]
		+ sistema["p24"] * sistema["p44"]))

	print("La probabilidad de morir en 2 dias desde estado ICU es: " +
		str(sistema["p30"] * sistema["p03"] + sistema["p31"] * sistema["p14"] 
		+ sistema["p32"] * sistema["p24"] + sistema["p33"] * sistema["p34"]
		+ sistema["p34"] * sistema["p44"]))
	
	'''Para calcular para los dias 4, 8 y 16 es el mismo procedimiento, se calcula 
	P**4 = P*P*P*P, P**8 = P*P*P*P*P*P*P*P, P**16 = P*P*P*P*P*P*P*P*P*P*P*P*P*P*P*P
	y luego se miran los valores de la ultima columna'''

	'''Vemos un grafico con el tiempo promedio hasta morir'''
	#Se muestran graficos para visualizar los resultados
	y = ["Sano","Infectado","Hospitalizado","ICU"]
	estados = [tsanoamorir, tinfectadoamorir, thospitalizadoamorir, ticuamorir]
	plt.ylabel('Cantidad de dias promedio')
	plt.xlabel('Estado inicial')
	plt.title("Dias promedio hasta morir")
	plt.bar(y,estados)
	plt.show()

	'''Analogamente vemos un grafico con la probabilidad de morir en 2 dias desde cada estado'''
	y = ["Sano","Infectado","Hospitalizado","ICU"]
	estados = [0, 0.0075, 0.0075, 0.27]
	plt.ylabel('Probabilidad')
	plt.xlabel('Estado inicial')
	plt.title("Probabilidad de morir en 2 dias partiendo de cada estado")
	plt.bar(y,estados)
	plt.show()

def estado_futuro(sistema,a,b,c,d):
	future = random.random()
	if (future < sistema[a]):
		return "Sano"
	elif (future < sistema[a] + sistema[b]):
		return "Infectado"
	elif (future < sistema[a] + sistema[b] + sistema[c]):
		return "Hospitalizado"
	elif (future < sistema[a] + sistema[b] + sistema[c] + sistema[d]):
		return "ICU"
	else:
		return "Dead"

def cambiar_estado(estado_actual, sistema):
	a = ""
	b = ""
	c = ""
	d = ""
	if (estado_actual == "Sano"):
		a = "p00"
		b = "p01"
		c = "p02"
		d = "p03"
	elif (estado_actual == "Infectado"):
		a = "p10"
		b = "p11"
		c = "p12"
		d = "p13"
	elif (estado_actual == "Hospitalizado"):
		a = "p20"
		b = "p21"
		c = "p22"
		d = "p23"
	elif (estado_actual == "ICU"):
		a = "p30"
		b = "p31"
		c = "p32"
		d = "p33"
	else:
		return "Dead"
	return estado_futuro(sistema,a,b,c,d)

def evolucion_sistema(sistema):
	#Estado inicial sano
	estado = "Sano"
	for i in range(10): #10 individuos
		print(Fore.WHITE + "Persona numero: " + str(i))
		print(Fore.GREEN + estado, end="")
		for j in range(100): #100 instantes de tiempo
			estado = cambiar_estado(estado,sistema)
			if (estado == "Sano"):
				print(" -> " + Fore.GREEN + estado, end="")
			elif (estado == "Infectado"):
				print(" -> " + Fore.YELLOW + estado, end="")
			elif (estado == "Hospitalizado"):
				print(" -> " + Fore.MAGENTA + estado, end="")
			elif (estado == "ICU"):
				print(" -> " + Fore.BLUE + estado, end="")
			else:
				print(" -> " + Fore.RED + estado, end="")
		print("\n\n")
		estado = "Sano"

def curvas_evolucion(poblacion,sistema):
	dias = 100 #tomamos 100 dias para la evaluacion
	estado = "Sano" #estado inicial
	cantidad_sanos = []
	cantidad_infectados = []
	cantidad_hospitalizados = []
	cantidad_icu = []
	cantidad_dead = []
	y = []

	for dia in range(dias):
		cantidad_sanos.append(0)
		cantidad_infectados.append(0)
		cantidad_hospitalizados.append(0)
		cantidad_icu.append(0)
		cantidad_dead.append(0)
		y.append(dia)

	for i in range(poblacion):
		for j in range(dias):
			if (estado == "Sano"):
				cantidad_sanos[j] += 1
			elif (estado == "Infectado"):
				cantidad_infectados[j] += 1
			elif (estado == "Hospitalizado"):
				cantidad_hospitalizados[j] += 1
			elif (estado == "ICU"):
				cantidad_icu[j] += 1
			else:
				cantidad_dead[j] += 1
			estado = cambiar_estado(estado,sistema)
		estado = "Sano"
		
	plt.xlabel('Dia')
	plt.ylabel('Cantidad de personas')
	plt.title("Cantidad de personas en estado Sano por dia")
	plt.plot(y,cantidad_sanos)
	plt.show()

	plt.xlabel('Dia')
	plt.ylabel('Cantidad de personas')
	plt.title("Cantidad de personas en estado Infectado por dia")
	plt.plot(y,cantidad_infectados)
	plt.show()

	plt.xlabel('Dia')
	plt.ylabel('Cantidad de personas')
	plt.title("Cantidad de personas en estado Hospitalizado por dia")
	plt.plot(y,cantidad_hospitalizados)
	plt.show()

	plt.xlabel('Dia')
	plt.ylabel('Cantidad de personas')
	plt.title("Cantidad de personas en estado ICU por dia")
	plt.plot(y,cantidad_icu)
	plt.show()

	plt.xlabel('Dia')
	plt.ylabel('Cantidad de personas')
	plt.title("Cantidad de personas en estado Dead por dia")
	plt.plot(y,cantidad_dead)
	plt.show()


def main():
	#Puntos A y B
	#sistema_verificacion(sistema, inversa)

	#PUNTO C
	#evolucion_sistema(sistema)

	#PUNTO D
	#curvas_evolucion(10000,sistema)

main()