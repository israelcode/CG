#x=int(input())
#for i in range(x):
#   print('%s%s' % (' ' * (x-i-1), '*' * (i*2+1)))

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Skeleton visualization of a polyhedron

Title = "Pyramid"

# Peaks of the pyramid
v = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1],  [-1, 1, -1], [0, 0, 1]])
ax.scatter(v[:, 0], v[:, 1], v[:, 2])

# Orthonormal projections
ax.plot([-1,1,0,-1], [-1,-1,1,-1], 'r', zdir='y', zs=1.5) 
ax.plot([-1,1,0,-1], [-1,-1,1,-1], 'g', zdir='x', zs=-1.5) 
ax.plot([-1,1,1,-1,-1], [1,1,-1,-1,1], 'k', zdir='z', zs=-1.5)

# Generate list of sides' polygons of our pyramid
verts = [ [v[0],v[1],v[4]], [v[0],v[3],v[4]],
 [v[2],v[1],v[4]], [v[2],v[3],v[4]], [v[0],v[1],v[2],v[3]]]

# Draw sides
ax.add_collection(Poly3DCollection(verts, 
 facecolors='cyan', linewidths=1, edgecolors='r'))

ax.add_collection(Line3DCollection(verts, colors='k', linewidths=0.2, linestyles=':'))

plt.title(Title,fontsize=20)
fig.canvas.set_window_title('Chekushkin')

#________________________________________________
# Cylinder
x=np.linspace(-1, 1, 100)
z=np.linspace(-2, 2, 100)
Xc, Zc=np.meshgrid(x, z)
Yc = np.sqrt(1-Xc**2)

# Draw parameters
rstride = 20
cstride = 10
ax.plot_surface(Xc, Yc, Zc, alpha=0.2)
ax.plot_surface(Xc, -Yc, Zc, alpha=0.2)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
#_________________________________________________________

plt.show()
