#numpy.org
#NUMPY BIDIMENSIONAL

#as Matrizes Numpy podem ter mais de uma dimensão.

import numpy as np
a=[[12,12,13],[21,22,23],[31,32,33]]
b=np.array(a)
b
#   array([[12, 12, 13],
#          [21, 22, 23],
#          [31, 32, 33]])    as linhas e colunas iniciam no Zero 0,1,2

b.ndim #quantas dimensões b possui? resul. é 2
b.shape #informa, o número de listas do array 3 (separadas por virgulas), e tbm informará o número de elementos dentro das listas (3).
b.size # soma o número de elementos das linhas e das colunas, result. 9

a[1][2] #linha 1, coluna 2 =23
a[0][0]
a[0][1]

x=np.array([[1,0],[0,1]])
y=np.array([[2,1],[1,2]])
z=x+y
z
#    array([[3, 1],
#          [1, 3]])
y
y*2

c=np.array([[0,1,1],[1,0,1]])
d=np.array([[1,1],[1,1],[-1,1]])
e=np.dot(c,d)
e
