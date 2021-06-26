import random
import matplotlib.pyplot as plt
import numpy as np
#2) Replicar los resultados del trabajo “A Markov Chain Model for Covid-19 Survival Analysis”
#A) Seccion 2.0: A Simple Markov Chain

'''En este caso se consideran tres estados: 0: Paciente sano. 1: Paciente infectado. 2: Paciente hospitalizado
El paciente no puede pasar de sano a hospitalizado, o viceversa, sin pasar por el estado infectado. El paciente
puede mantenerse en el mismo estado.
A su vez se tiene una matriz P donde se modela la matriz de transición de probabilidad de Markov '''

#!!!!!!!!!!!!!!!!!!!!!!
#INCLUIR FOTO DEL PAPER DONDE MUESTRA EL DIAGRAMA!!!!!! Y LA MATRIZ P
#!!!!!!!!!!!!!!!!!!!!!!

'''Contamos con dos sistemas de Markov, uno llamado eficiente y uno llamado no eficiente. El paper nos comenta
y nos permite ver que el sistema eficiente, a la larga en el tiempo, mantiene una mayoria de pacientes sanos
y pocos hospitalizados. Mientras que en el sistema ineficiente se mantienen relativamente pocos sanos y muchos 
mas hospitalizados.'''

#!!!!!!!!!!!!!!!!!!!!!!
#INCLUIR FOTO DEL PAPER DONDE MUESTRAN LOS SISTEMAS
#!!!!!!!!!!!!!!!!!!!!!!

'''Tambien podemos ver que en el sistema eficiente, el tiempo promedio entre dos pacientes hospitalizados es mucho
mayor al tiempo promedio entre dos pacientes sanos. En el sistema ineficiente estos valores son mucho mas parecidos
entre si, lo cual logicamente seria preocupante.
'''

#!!!!!!!!!!!!!!!!!!!!!!
#INCLUIR FOTO DEL PAPER DE LA TABLA 1
#!!!!!!!!!!!!!!!!!!!!!!


'''La diferencia fundamental entre los sistemas es que en el eficiente la probabilidad de mantenerse sano es 
de 95% mientras que en el eficiente es del 90%, y en el eficiente la probabilidad de seguir en el hospital
es de "solo" el 70% mientras que en el ineficiente es del 80%'''

''' ARMAMOS LA MATRIZ DE PROBABILIDADES '''
eficiente = {"p00" : 0.95, "p01" : 0.05, "p02" : 0,
			"p10": 0.10, "p11" : 0.70, "p12" : 0.2,
			"p20": 0, "p21": 0.30, "p22": 0.7}

ineficiente = {"p00" : 0.9, "p01" : 0.1, "p02" : 0,
			"p10": 0.12, "p11" : 0.70, "p12" : 0.18,
			"p20": 0, "p21": 0.2, "p22": 0.8}		

def estado_futuro(sistema,a,b):
	future = random.random()
	if (sistema[a] > future):
		return "Sano"
	elif (sistema[a] + sistema[b]) < future:
		return "Hospitalizado" 
	else:
		return "Infectado"

def cambiar_estado(estado_actual, sistema):
	a = ""
	b = ""
	if (estado_actual == "Sano"):
		a = "p00"
		b = "p01"
	elif (estado_actual == "Infectado"):
		a = "p10"
		b = "p11"
	else:
		a = "p20"
		b = "p21"
	return estado_futuro(sistema,a,b)

def sistema_eficiente(N):
	estados = [1,0,0]
	estado = "Sano" #arrancamos en paciente sano
	for_graph = []
	for i in range(N):
		estado = cambiar_estado(estado,eficiente)
		if (estado == "Sano"):
			estados[0] += 1
			for_graph.append("Sano")
		elif (estado == "Infectado"):
			estados[1] += 1
			for_graph.append("Infectado")
		else:
			estados[2] += 1
			for_graph.append("Hospitalizado")
	
	print("Se muestra el porcentaje de tiempo que pasa el paciente en cada estado en regimen:")
	print("El porcentaje de sanos es " + str((estados[0]/N) * 100) + "%")
	print("El porcentaje de infectados es " + str((estados[1]/N) * 100) + "%")
	print("El porcentaje de hospitalizados es " + str((estados[2]/N) * 100) + "%")

	print("")

	print("Se muestra el tiempo promedio entre dos visitas sucesivas a cada estado:")
	print("T0 (Sanos): " + str(1/(estados[0]/N)))
	print("T1 (Infectados) " + str(1/(estados[1]/N)))
	print("T2 (Hospitalizados) " + str(1/(estados[2]/N)))
	
	''' Obtuvimos:
	El porcentaje de sanos es 54.8018%
	El porcentaje de infectados es 27.1754%
	El porcentaje de hospitalizados es 18.0229%

	T0 (Sanos): 1.82475758095537
	T1 (Infectados) 3.6797986414183415
	T2 (Hospitalizados) 5.548496634836791

	Que es practicamente el resultado del paper para el sistema eficiente '''

	#Se muestran graficos para visualizar los resultados
	y = ["Sano","Infectado","Hospitalizado"]
	plt.ylabel('Cantidad')
	plt.xlabel('Estado')
	plt.title("Cantidad de veces en cada estado")
	plt.bar(y,estados)
	plt.show()

	plt.title("Estado por unidad de tiempo")
	plt.xlabel("Tiempo")
	plt.ylabel("Estado")
	plt.plot(for_graph)
	plt.show()

def sistema_ineficiente(N):
	estados = [1,0,0]
	estado = "Sano" #arrancamos en paciente sano
	for_graph = []
	for i in range(N):
		estado = cambiar_estado(estado,ineficiente)
		if (estado == "Sano"):
			estados[0] += 1
			for_graph.append("Sano")
		elif (estado == "Infectado"):
			estados[1] += 1
			for_graph.append("Infectado")
		else:
			estados[2] += 1
			for_graph.append("Hospitalizado")
	
	print("Se muestra el porcentaje de tiempo que pasa el paciente en cada estado en regimen:")
	print("El porcentaje de sanos es " + str((estados[0]/N) * 100) + "%")
	print("El porcentaje de infectados es " + str((estados[1]/N) * 100) + "%")
	print("El porcentaje de hospitalizados es " + str((estados[2]/N) * 100) + "%")

	print("")

	print("Se muestra el tiempo promedio entre dos visitas sucesivas a cada estado:")
	print("T0 (Sanos): " + str(1/(estados[0]/N)))
	print("T1 (Infectados) " + str(1/(estados[1]/N)))
	print("T2 (Hospitalizados) " + str(1/(estados[2]/N)))
	
	''' Obtuvimos:
	El porcentaje de sanos es 38.3897%
	El porcentaje de infectados es 32.3078%
	El porcentaje de hospitalizados es 29.3026%

	Se muestra el tiempo promedio entre dos visitas sucesivas a cada estado:
	T0 (Sanos): 2.604865367533479
	T1 (Infectados) 3.0952277778121693
	T2 (Hospitalizados) 3.4126664528062354


	Que es practicamente el resultado del paper para el sistema eficiente '''

	#Se muestran graficos para visualizar los resultados
	y = ["Sano","Infectado","Hospitalizado"]
	plt.ylabel('Cantidad')
	plt.xlabel('Estado')
	plt.title("Cantidad de veces en cada estado")
	plt.bar(y,estados)
	plt.show()

	plt.title("Estado por unidad de tiempo")
	plt.xlabel("Tiempo")
	plt.ylabel("Estado")
	plt.plot(for_graph)
	plt.show()

def main():
	#Contamos la cantidad de tiempos que el paciente pasa en cada estado
	#Con un número suficientemente grande podemos aproximar el vector Pi

	N = 1000000 #iteraciones
	#sistema_eficiente(N)
	#sistema_ineficiente(N)


main()