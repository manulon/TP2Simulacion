import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
plt.style.use("bmh")

'''3) Se desea simular la evolución de una epidemia utilizando el modelo S.I.R.
Se conoce que inicialmente el 3% de la población se encuentra infectada, toda la población es susceptible de
contagiarse, la tasa de transmisión α=0,27, y la tasa de recuperación β = 0,043'''

#Modelo matemático SIR (contagio entre personas):
'''
Tenemos tres variables y por ende tres ecuaciones diferenciales:
S(t): Susceptibles --> dS/dt = -alpha*S*I
I(t): Infectados --> dI/dt = alpha*S*I - beta*I
R(t): Recuperados --> dR/dt = beta*I
'''

# Las ecuaciones diferenciales del modelo SIR
def deriv(y, t, N, beta, alpha):
    S, I, R = y
    dSdt = -alpha*S*I/N
    dIdt = alpha*S*I/N - beta*I
    dRdt = beta*I
    return dSdt, dIdt, dRdt

def plot(S, I, R, t, divide_by):
    # Dibujamos los datos de S(t), I(t) y R(t)
    #fig, ax = plt.subplots()
    plt.plot(t, S/divide_by, 'b', alpha=0.5, lw=2, label='Susceptible')
    plt.plot(t, I/divide_by, 'r', alpha=0.5, lw=2, label='Infectado')
    plt.plot(t, R/divide_by, 'g', alpha=0.5, lw=2, label='Recuperado')
    plt.axhline(y=0.30,linewidth=1,color='black',label='Max. cap. sistema de salud')
    plt.xlabel('Días')
    plt.ylabel('Cantidad de personas')
    plt.title("Cantidad de personas en cada estado por dia")
    legend = plt.legend()
    plt.show()

def modelo_sir(alpha,beta,poblacion,avgcontagiados):
	contagiados_inicial = avgcontagiados * poblacion
	s0 = poblacion - contagiados_inicial
	i0 = contagiados_inicial
	r0 = 0

	y0 = s0, i0, r0
	# Pasos temporales (en días)
	t = np.linspace(0, 200, 200)

	 #Integrate the SIR equations over the time grid, t.
	ret = odeint(deriv, y0, t, args=(poblacion, beta, alpha))
	S, I, R = ret.T

	plot(S, I, R, t, poblacion) # Datos normalizados

def main():
	#Parametros
	alpha = 0.27
	beta = 0.043
	poblacion = 10000
	modelo_sir(alpha,beta,poblacion,0.03)

	'''Vemos que con este juego de datos se supera la capacidad maxima del sistema de salud,
	queremos corregir esto'''
	'''
	Tenemos que modificar los parametros para lograr esto. Que significa cada parametro?
	Alpha = Nos indica cuan facil es que un miembro de la población I infecte a un miembro de la población S.
	Beta = El parámetro gamma nos indica la facilidad de que un miembro de la población I se recupere.
	Entonces deberiamos reducir alpha y/o aumentar beta
	'''

	alpha = 0.14
	beta = 0.048
	poblacion = 10000
	modelo_sir(alpha,beta,poblacion,0.03)
	'''De esta forma no se supera la capacidad del sistema de salud y la epidemia dura aprox. 175 dias
	La pandemia dura mas dias pero el sistema de salud no colapsa. Si se quisiese que la pandemia
	dure lo menos posible, la capacidad del sistema de salud se veria excedida por mucho.'''

	'''Cuanto tendriamos que modificar uno solo de los parametros para no saturar el sistema de salud?'''
	alpha = 0.27
	beta = 0.092
	poblacion = 10000
	modelo_sir(alpha,beta,poblacion,0.03)
	#Aprox 85 dias

	alpha = 0.125
	beta = 0.043
	poblacion = 10000
	modelo_sir(alpha,beta,poblacion,0.03)
	#Aprox 200 dias

	#Conviene aumentar beta antes que reducir alpha en base a los comportamientos explorados

	'''Que pasa con los nuevos parametros de los ultimos dos sets?'''
	alpha = 0.125
	beta = 0.092
	poblacion = 10000
	modelo_sir(alpha,beta,poblacion,0.03)
	#Aprox 150 dias pero muy pocos contagiados


	'''Los resultados son similares al ejercicio 2 en cuanto a la velocidad y forma de las curvas
	para los contagios de la población, pero difieren en el momento de la recuperación de los pacientes,
	basicamente porque en el ejercicio 2 no obtenian inmunidad, por lo que cuando se llegaba a un pico
	de contagios se mantenia la curva ahi, e incluso morian, a diferencia de aqui que una vez curados
	se vuelven inmunes a la enfermedad, y no pueden morir. Entonces la curva de susceptibles/sanos si se 
	asemeja al ejercicio 2, pero la curva de infectados no lo hace, y tampoco la curva de recuperados
	que no existia en el ejercicio anterior.
	'''

main()