"""cosine response """

from numpy import zeros,cos,pi,linspace
from scipy.signal import lfilter
import matplotlib.pyplot as plt

N=int(input('response length:'))
b=[1.0] #this can be changed depending on your transfer function
a=[1.0,-0.8] #this can be changed depending on your transfer function
n=linspace(0,N-1)
x=cos(0.05*pi*n)
y=lfilter(b,a,x)

plt.stem(n,x)
plt.title('sinusoidal input')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.show()

plt.stem(n,y)
plt.title('output')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.show()