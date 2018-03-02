import matplotlib.pyplot as plt
from math import cos, sin, pi, sqrt
from numpy import linspace

x = []
y = []
for theta in linspace(0,2*pi,num=1000):
    r = (10**(-6)/sqrt(0.9))-(82/9)*cos(sqrt(0.9)*theta)+100/9
    x.append(r*cos(theta))
    y.append(r*sin(theta))

plt.plot(x,y)
plt.show()



x = []
y = []
for theta in linspace(0,2*pi,num=1000):
    r = 5*theta**2 + 10**-6*theta + 2
    x.append(r*cos(theta))
    y.append(r*sin(theta))

plt.plot(x,y)
plt.show()





