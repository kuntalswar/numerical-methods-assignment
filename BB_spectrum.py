import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

#Data taking as input from .txt file
frequency = np.loadtxt('nasa.txt', usecols = 0)
cmb_flux = np.loadtxt('nasa.txt', usecols = 1)

#defining constants
c = 3.e8
T = 2.725
h = 6.626*10**(-34)
k = 1.38*10**(-23)

frequency = frequency*c*100#changing frequency from (cm)^-1 to Hz

BB = (2.0*h*(frequency**3)/(c**2))*(1.0/(np.exp(frequency*h/(k*T))-1.0))#Black body radiation formula

peaks,_=find_peaks(BB)
print("The wavelength corresponding to the peak is ", 299792458/frequency[peaks],"m")
print("It is in the microwave region")

#Ploting the spectrum
plt.plot(frequency, cmb_flux*(10**(-20)),'k.',label = 'CMB Data')
plt.plot(frequency, BB,'r-', label = 'BB spectrum')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Flux(SI unit)')
plt.legend()
plt.show()



