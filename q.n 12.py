#Plot the space curve 𝑥 = 2θcos 𝜃, 𝑦 = 2θsin 𝜃, 𝑧 = 1 + 2 𝜃 𝑓𝑜𝑟 0 ≤ 𝜃 ≤ 20𝜋

from mpl_toolkits import mplot3d
from numpy import *
from matplotlib.pyplot import *
fig=figure(figsize=(8,5))
ax=axes(projection='3d')

theta=linspace(0,20*pi,1000);
x=2*theta*cos(theta)
y=2*theta*sin(theta)
z=1+2*theta

ax.plot3D(x,y,z,'g')
ax.scatter3D(x,y,z)
show()

