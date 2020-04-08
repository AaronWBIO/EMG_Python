#from time import time
import time
import serial
import numpy as np 

import os
import sys


arduino = serial.Serial('COM4', 115200)
time.sleep(1)
#a = np.array([])
lista = []

cont = 0
print('inicio')
tiempo_inicial = time.time()
while True:
  line = arduino.readline().strip().decode('ascii')

  #print(line)
  #a = np.insert(a,cont,line)
  lista.append(line)

  cont = cont+1
  if cont > 10000:
    break
tiempo_final = time.time()
tiempo_ejecucion = tiempo_final - tiempo_inicial
print ('El tiempo de ejecucion fue:',tiempo_ejecucion+1) #tiempo en segundos

arduino.close()  
print('fin')
a = np.asarray(lista)
y = a.astype(np.float)
#print(a)
np.savetxt('registro.txt', y, delimiter ='\n')  