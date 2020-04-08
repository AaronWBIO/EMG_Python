from time import time
from time import sleep
import serial
import numpy as np 
arduino = serial.Serial('COM4', 115200)

sleep(2)
#a = np.array([])
lista = []
cont = 0


def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

print('inicio')
tiempo_inicial = time() 
while True:
  if arduino.inWaiting():
    line = arduino.readline().strip().decode('ascii','ignore')
    #print(line)
    #a = np.insert(a,cont,line)

    if isfloat(line) == True:
      lista.append(line)
      cont = cont+1
    if cont > 10000:
      break
    
tiempo_final = time() 
tiempo_ejecucion = tiempo_final - tiempo_inicial
print ('El tiempo de ejecucion fue:',tiempo_ejecucion+2) #tiempo en segundos

arduino.close()  
print('fin')
a = np.asarray(lista)
y = a.astype(np.float)
#print(a)
np.savetxt('registro.txt', y, delimiter ='\n',fmt = "%f")