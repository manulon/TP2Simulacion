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
	#PUNTO C
	#evolucion_sistema(sistema)

	#PUNTO D
	#curvas_evolucion(10000,sistema)

main()