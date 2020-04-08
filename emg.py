import emg_DSP

import matplotlib.pyplot as plt
import numpy as np

import scipy as sp
from scipy import signal

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


Fs = 1000                                       #frecuencia de muestreo 1kHz
data = np.loadtxt("emg1.txt", delimiter='\n')   #leer archivo txt
tiempo =  np.arange(0, len(data)/Fs, 1/Fs)      #crear arreglo de tiempo

emg = data*3.3/4095                            #convertir a voltaje

emg_zero = emg - np.mean(emg)

# filtro
emg_filtered = emg_DSP.band_pass_filter(20,450, Fs, emg_zero)
emg_envelope = emg_DSP.envelope(emg_filtered, 5, Fs)

#plt.plot(tiempo,emg_filtered)                           #graficar
#plt.ylabel('Amplitud (V)')                      #etiqueta eje Y
#plt.xlabel('Tiempo(s)')                         #etiqueta eje X
#plt.show()

#media = np.mean(emg_envelope)
#desv = np.std(emg_envelope)

#linea_std = emg_envelope
#linea_std[:]=desv 
#print(len(emg_filtered))
#print(len(linea_std))


plt.plot( emg_filtered)                           #graficar
#plt.plot(tiempo,emg_envelope,'r')
#plt.ylabel('Amplitud (V)')                      #etiqueta eje Y
#plt.xlabel('Tiempo(s)')                         #etiqueta eje X
plt.show()




s1 = emg_filtered[1806:2560]
s2 = emg_filtered[4000:4955]

plt.plot(s1)  
plt.plot(s2,'r')                          #graficar
plt.show()

s1_mav = emg_DSP.MAV(s1)
