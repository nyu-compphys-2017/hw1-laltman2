from numpy import loadtxt
from pylab import plot, show


data = loadtxt("millikan.txt", float)

x = data[:,0]
y = data[:,1]

N = len(x)

Ex = sum(x)/N
Ey = sum(y)/N
Exx = sum(map(lambda i:i**2, x))/N

Exy = 0
for i in range(N):
    Exy += x[i]*y[i]
Exy = Exy/N

m = (Exy-Ex*Ey)/(Exx-Ex**2)
c = (Exx*Ey - Ex*Exy)/(Exx-Ex**2)

yfit = list(map(lambda i: (m*i+c), x))

echarge = 1.602*10**(-19)

Planckexp = m*echarge

print(m)
print(c)
print(Planckexp)

plot(x,yfit)
plot(x,y,"ko")
show()
