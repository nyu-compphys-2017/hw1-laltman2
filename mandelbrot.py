import numpy as np
from pylab import imshow, show

#metafunction which computes the equation
def metamandel(z, c):
    return (z**2 + c)

#recursive function, returns 0 if z>=2 ever, 1 if
#finishes the recursion never exceeding 2
def mandelbrot(z,c,n):
    if (np.absolute(z) >= 2):
        return 0
    elif (n==0):
    	return 1
    else:
    	return mandelbrot(metamandel(z,c), c, n-1)

#vectorize the function
vmandelbrot = np.vectorize(mandelbrot)

#construct NxN grid of complex values, map function to grid
def mapping(N):
    table = np.zeros((N,N),dtype = np.complex_)
    dataset = np.zeros((N,N))
    step = 4/float(N-1)
    for x in range(N):
        for y in range(N):
            table[x,y] = (step*x-2) + 1j*(step*y-2)
            dataset[x,y] = vmandelbrot(0,table[x,y],100)
    return dataset
   
data = mapping(1000)
imshow(data)
show()
