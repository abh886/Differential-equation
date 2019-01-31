from numpy import ones
from scipy.signal import lfilter
import matplotlib.pyplot as plt

N=int(input('response length:'))
b=[1.0]
a=[1.0,-1.0,0.9]
x=ones(N)

y=lfilter(b,a,x)


plt.stem(x)
plt.title('step response')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.show()

plt.stem(y)
plt.title('output')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.show()