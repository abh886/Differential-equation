"""problem 4 """

from numpy import cos,pi,linspace
from scipy.signal import lfilter_zi,lfilter,lfiltic
import matplotlib.pyplot as plt

N=int(input('response length:'))
b=[0.33,0.33,0.33]
a=[1.0,-0.95,0.9025]

n=linspace(0,N-1)

x=cos(0.05*pi*n)

A=[1,1]
B=[2,2]

zi=lfilter_zi(B,A)
y=lfilter(b,a,x,zi)



plt.stem(n,x)
plt.title('input')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.show()

plt.stem(n,y)
plt.title('output')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.show()

