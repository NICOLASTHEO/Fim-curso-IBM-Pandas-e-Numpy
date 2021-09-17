# NUMPY - TODOS OS ELEMENTOS INTERNOS SERÃO DO MESMO TIPO, EX.: TODOS INTEIROS.
#NÃO SE MISTURAM EM NUMPY INTEIROS COM STR,  COMO EM UMA LISTA.
# NUMPY UNIDIMENSIONAL
import matplotlib
import numpy as np
#lista
a=[0,'1',"two","3",4]
a # em listas podem haver intergers, float, e strings juntos.

a=np.array([0,1,2,3,4]) #todos elementos do mesmo tipo, aqui inteiros/integers
type(a) #DEVOLVE-SE O TIPO DO ARRAY --> resultado é numpy .ndarray
a.dtype #DEVOLVE O TIPO DO ARRAY NUMPY --> resultado: dtype é = int de 64
a.size #devolve a quantidade de elementos dentro do array --> 5
a.ndim #informa a quantidade de dimensões do Array --> 1, uma dimensão
a.shape #informa a quantidade de elementos dentro de cada dimensão. -->5,...
b=np.array([3.1,11.02,6.2,213.2,5.2])
type(b)
b.dtype #informará que isto é um FLOAT
#PODEMOS MUDAR OS ELEMENTOS DENTRO DO ARRAY
c=np.array([20,1,2,3,4])
c #aray([20,1,2,3,4])
c[0]=100
c # o novo valor será array([100,1,2,3,4])
c[4]=0
c #novo valor será array([100,1,2,3,0])

#DIVIDINDO O ARRYA EM NOVOS ARRAYS
d=c[1:4]
d #teremos um novo array, d=array([1,2,3])
c
c[3:5]=300,400 #mudará os valores so array, mudará dois concomitantemente
c #novo valor de 'c' será array([100,1,2,300,400])
u=[0,1]
v=[1,0]
z=[]
for n,m in zip (u,v):
    z.append(n+m)
    print(z) #result 1,1
#são coisas diferentes: 'for' e 'np', mas o resultado é mesmo
u=np.array([1,0])
v=np.array([0,1])
z=u+v
z #result é array([1,1])
#podemos realizar subtrações:
u=np.array([1,0])
v=np.array([0,1])
z=u-v
z   #1,-1
#ou ainda por 'for'
u=[1,0]
v=[0,1]
z=[]
for i,j in zip(u,v):
    z.append(i-j)
    print(z) #1,-1

#MULTIPLICAÇÃO com SCALAR
y=np.array([1,2])
z=2*y
z #resultado array([2,4])
# com FOR
y=[1,2]
z=[]
for i in y:
    z.append(2*i)
    z #resultado é z= 2,4

#PRODUTO '*'DE DOIS ARRAYS
u=np.array([1,2])
v=np.array([3,2])
z=u*v
z #resultado é array([3,4])
# com FOR
u=[1,2]
v=[3,2]
z=[]
for i,j in zip(u,v):
    z.append(i*j)
    z #resultado é 3,4
# DOC PRODUCT
#mostra a similaridade entre os produtos, primeiro multiplica-os e depois soma os resultados.
#ex.:
u=np.array([1,2])
v=np.array([3,1])
result=np.dot(u,v)
result #o número similiar entre os produtos '*' entre eles é 5, primeiro eles se multiplicam em linha reta e os resultados são somados.

#com FOR
u=[1,2]
v=[3,1]
for i,j in zip(u,v):
    np.dot(u,v)
#result é 5

#adicionando uma constante a um NUMPY Array
u=np.array([1,2,3,-1])
z=u+1 # o Numpy adicionará a cada elemento do ARRAY
z #resultado é array([2,3,4,0])

# FUNÇÕES UNIVERSAIS
# função -->   MEAN
a=np.array([1,-1,1,-1])
mean_a=a.mean()
mean_a # Mean informa a média dos números do Array, resultado é 0.0
b=np.array([1,-2,3,4,5])
max_b=b.max() 
max_b#max informa o maior valor existente
min_b=b.min()
min_b#min informa o menor valor existente no array
select=[0,2,3]  # a lista SELECT contem vários valores que poderão ser indexados
d=c[select]
d
c[select]=10000
c

standard_deviation=b.std() #deviation informa o desvio padrão da matriz em uso
standard_deviation
#podemos calcular o PI em numpy
np.pi
#valor de PI = 3,14
x=np.array([0,np.pi/2,np.pi])
y=np.sin(x) #sin mapeia os valores - sin noo array x atribui o valor ao array y; isso aplica a função SENO a cada elemento da matriz
y # resultado é y=array([0,1,1.2e-16])

#PODEMOS SUBDIVIDIR VALORES UNICOS DENTRO DE PERÍODOS. eX.:
# LIN SPACE
np.linspace(-2,2,num=5) # dentro do intervalo de -2 e 2 nos será informado o total de 5 valores.
# array([-2,-1,0,1,2])
np.linspace(-2,2,num=9)#informação de 9 elementos dentro de -2 até 2
#array([-2,-1.5,-1,-0.5,0,0.5,1,1.5,2])

x=np.linspace(0,2*np.pi,100)
y=np.sin(x)  #sin irá mapear o array X até o novo array Y
# para plotar o resultados USAR A BIBLIOTECA MATPLOTLIB
import matplotlib.pyplot as plt
#se estiver usando o JUPYTER o comando será: %matplotlib inline
#agora basta plotar o resultado
plt.plot(x,y)
#Exercícios:
#1
a=np.array([1,1,1,1,1])
b=np.array([2,2,2,2,2])
a*b   #2,2,2,2,2

#2
a=np.array([-1,1])
b=np.array([1,1])
np.dot(a,b) # 0

#3
a=np.array([1,1,1,1,1])
a+10 # 11,11,11,11,11

