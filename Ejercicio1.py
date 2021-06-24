import numpy as np
import matplotlib.pyplot as mp

# Simule el siguiente problema.
# Se está diseñando un web service, el cual cada vez que es invocado consulta a una base de datos.
# El tiempo que transcurre entre cada llamada al servicio se puede modelar según una distribución 
# exponencial con media μ. Considerar μ = 1, 2 y 4 segundos

# Utilizar 1 base de datos central.
# En este caso la demora en resolver una solicitud sigue una distribución exponencial 
# con μ = 0,8 segundos

# Realizar 100 simulaciones de cada modelo, con 100000 solicitudes procesadas, y determinar:
# + El tiempo medio de espera entre que la solicitud llega y puede ser procesada 
# (suponer que ninguna conexión se cae por timeout).
#   + La fracción de las solicitudes que no esperaron para ser procesadas.

# + La tasa de finalización de consultas (consultas finalizadas por segundo)
#   + ¿Qué solución le recomienda? Justifique

#---------------------------------------------------#

mu_tiempo_entre_llamadas = 1        # (segundos)
mu_demora_resolver_solicitud = 0.8  # (segundos)

n=100000

# Genero tiempos de llamadas
z = np.random.exponential(mu_tiempo_entre_llamadas, n)
tiemposLlamadas = np.concatenate(([0], np.cumsum(z)), axis=None)

#print ("Imprimo")
#print (tiemposLlamadas)
#print ("Listo")
