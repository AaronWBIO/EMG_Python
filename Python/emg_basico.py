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


plt.plot(tiempo, emg_zero, 'b')             #graficar
plt.ylabel('Amplitud (V)')                      #etiqueta eje Y
plt.xlabel('Tiempo(s)')                         #etiqueta eje X
plt.show()


emg_filtrada = emg_DSP.






