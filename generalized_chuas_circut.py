import matplotlib.pyplot as plt
import numpy as np

# https://people.eecs.berkeley.edu/~chua/papers/Brown93.pdf
# https://www.cedrick.ai/posts/attractors.html

def chua(xyz,*,a=9.0,bb=14.286, cc=0.0, alpha=-0.8, beta=0.3): # b = 0.208186 or 0.32899 or 0.1225 or else
    x, y, z = xyz
    """
    h=0
    if x >= 1.0:
        h = beta*x + alpha - beta
    if abs(x) < 1.0:
        h = alpha*x
    if x <= - 1.0:
        h = beta*x - alpha +beta
    --------------------------------------------------------------------------------
    """
    m = [-1/7,2/7,-4/7,2/7,-4/7,2/7]
    b = [1.0,2.15,3.6,8.2,13.0]
    sum_h = 0
    for i in range(1,6):
        sum_h = sum_h + (m[i-1]-m[i])*(abs(x+b[i-1]) - abs(x-b[i-1]))
    h = m[5]*x + 0.5 * sum_h    
    """
    h = beta*x + 0.5 * (alpha - beta)*(abs(x+1.0) - abs(x-1.0)) 
    """
    
    x_dot = a*(y - h)
    y_dot = x-y+z
    z_dot = -bb*y - cc*z
    return np.array([x_dot, y_dot, z_dot])


dt = 0.01
num_steps = 100000

xyzs = np.empty((num_steps + 1, 3))
xyzs[0] = (0.1, 1., 1.05) 

for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + chua(xyzs[i]) * dt

# Plot
ax = plt.figure(dpi=200).add_subplot(projection='3d')
ax.plot(*xyzs.T, lw=0.05)
ax.axis('equal')
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Generalized Chua's Circut (Attractor)")

plt.show()
