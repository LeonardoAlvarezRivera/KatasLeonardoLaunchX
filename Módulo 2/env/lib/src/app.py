from datetime import * #importar todo del paquete datetime
from dateutil.relativedelta import * 
now = datetime.now() #se obtiene la hora actual
print(now) #imprime la hora actual

now = now + relativedelta(months=1, weeks=1, hour=10) #le suma a la hora actual un mes con 1 semana y 10 horas

print(now) #imprime la nueva hora 
