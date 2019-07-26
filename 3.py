#coding=utf-8
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LightSource

print("Please enter accuracy of approximation eps(0<eps<1):")

eps=float(input()) #Точность аппроксимации	
n=3 		   #Мин количество сторон
r=1 		   #Радиус круга в основании
alpha = 2*math.pi/n;

length_of_side = r * math.sqrt(2-2*math.cos(alpha)) 
height = length_of_side/2/math.tan(alpha/2)

while r - height > eps: #Аппроксимация
    n += 1
    alpha  = 2*math.pi/n
    length_of_side = r * math.sqrt(2-2*math.cos(alpha))
    height = length_of_side/2/math.tan(alpha/2)


g=360/(n)
#print("g=",g)
lx=[] #Список координат многогранника в основании(Ось Х)
ly=[] #Список координат многогранника в основании(Ось У)
ga=g

while (ga <= 360):  #Расчет координат
	x=math.cos(math.radians(ga))
	y=math.sin(math.radians(ga))
	lx.append(x)
	ly.append(y)
	ga=ga+g	
	if (ga>360): break
lx.append(lx[0])
ly.append(ly[0])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#ax.plot(lx,ly, 'r') #Построение многоугольника в основании


lxyz=[] #Список ребер многоугольника
i=0
while i < len(lx):
	lxyz.append([0,0,1])
	lxyz.append([lx[i],ly[i],0])
	i=i+1
	if (i>len(lx)): break

v=[]
z=0

while z<(len(lx)-1):#Список боковых граней многоугольника
	v.append([ [lx[z],ly[z],0], [0,0,1], [lx[z+1],ly[z+1],0]])	
	z=z+1

v2=[]
j=0
while j < (len(lx)):#Нижняя грань
	v2.append([lx[j],ly[j],0])
	j=j+1 


v.append(v2)

X = np.arange(-0.5, 0.5, 0.01)
xlen = len(X)
Y = np.arange(-0.5, 0.5, 0.01)
ylen = len(Y)

X, Y = np.meshgrid(X, Y)

colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)

#for y in range(ylen):
#    for x in range(xlen):
	#colors[x, y] = colortuple[(x + y)% 2] 
	#print(x,y,colors[x, y])

#Построение цилиндра
x=np.linspace(-1, 1, 100)
z=np.linspace(0, 1, 100)
Xc, Zc=np.meshgrid(x, z)
Yc = np.sqrt(1-Xc**2)

# Create light source object.
ls = LightSource(azdeg=0, altdeg=65)
# Shade data, creating an rgb array.
rgb = ls.shade(Yc, plt.cm.RdYlBu)

rstride = 20
cstride = 10
ax.plot_surface(Xc, Yc, Zc,facecolors=rgb, alpha=0.9,linewidth=0)
ax.plot_surface(Xc, -Yc, Zc,facecolors=rgb, alpha=0.9,linewidth=0)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.add_collection3d(Poly3DCollection(v, facecolor = 'blue', edgecolor = 'r', alpha = 1))

for b in range(ylen):
    for a in range(xlen):
	colors[a, b] = 0 
ax.plot_surface(Xc, Yc, Zc,facecolors=colors, alpha=0.9,linewidth=0)
#ax.plot_surface(Xc, -Yc, Zc,facecolors=rgb, alpha=0.9,linewidth=0)		


plt.show()
