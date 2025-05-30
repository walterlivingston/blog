import numpy as np
import matplotlib.pyplot as plt

# generate random points
n = 1000
mean = [3,4]
sigma = [0.5, 1]
data = np.random.normal(loc=mean, scale=sigma, size=(n,2))
data = data.T

# rotate points
theta = np.deg2rad(20)
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
rot_data = R @ data

plt.figure()
plt.scatter(rot_data[0, :], rot_data[1, :], alpha=0.7, edgecolors='k', zorder=2)
plt.title("Step 1: Sample Data")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True, zorder=0)
plt.axis('equal')
# plt.show()

# principal component analysis
P = np.cov(rot_data)
D, V = np.linalg.eig(P) # D is the eigenvalues, V is the eigenvectors

# axis-align data
mu = np.mean(rot_data, axis=1)
centered_data = np.transpose(rot_data.T - mu)
aa_points = V.T @ centered_data

plt.figure()
plt.scatter(rot_data[0, :], rot_data[1, :], alpha=0.7, edgecolors='k', zorder=2, label='Sampled')
plt.scatter(aa_points[0, :], aa_points[1, :], alpha=0.7, edgecolors='k', zorder=2, label='Axis-Aligned')
plt.title("Step 3: Axis-Aligned Data")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True, zorder=0)
plt.axis('equal')
# plt.show()

# axis-aligned bounding box
mx = np.max(aa_points, axis=1)
mn = np.min(aa_points, axis=1)
sz = mx - mn
x = np.array([mn[0], (mn[0] + sz[0])])
y = np.array([mn[1], (mn[1] + sz[1])])
pts = np.array([[x[0], x[1], x[1], x[0], x[0]],
                [y[0], y[0], y[1], y[1], y[0]]])

# axis-aligned bounding ellipse
tolerance = 1
eigenvalues = ((np.sqrt(2 + (tolerance*2))/(sz))**2)
S_aabe = np.diag(eigenvalues)

eigVals, eigVecs = np.linalg.eig(S_aabe)
t = np.linspace(0, 2 * np.pi, 1000)
circle = np.array([np.cos(t), np.sin(t)])
aa_ellipse = np.diag(1/np.sqrt(eigVals)) @ circle

plt.figure()
plt.scatter(rot_data[0, :], rot_data[1, :], alpha=0.7, edgecolors='k', zorder=2, label='Sampled')
plt.scatter(aa_points[0, :], aa_points[1, :], alpha=0.7, edgecolors='k', zorder=2, label='Axis-Aligned')
plt.plot(pts[0,:], pts[1,:], '-k', zorder=2, label='Bounding Box')
plt.plot(aa_ellipse[0], aa_ellipse[1], 'r-', zorder=2, label='Bounding Ellipse')
plt.title("Step 4: Axis-Aligned Bounding Box & Ellipse")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True, zorder=0)
plt.axis('equal')
# plt.show()

# oriented bounding box
obb_pts = V @ pts
obb_pts = np.transpose(obb_pts.T + mu)
S_obe = V @ np.diag(eigenvalues) @ V.T

# plot ellipse
eigVals, eigVecs = np.linalg.eig(S_obe)
o_ellipse = np.transpose(np.transpose(eigVecs @ aa_ellipse) + mu)

# plot
plt.figure()
plt.scatter(rot_data[0, :], rot_data[1, :], alpha=0.7, edgecolors='k', zorder=2, label='Sampled')
plt.scatter(aa_points[0, :], aa_points[1, :], alpha=0.7, edgecolors='k', zorder=2, label='Axis-Aligned')
plt.plot(pts[0,:], pts[1,:], '-k', zorder=2, label='AABB')
plt.plot(aa_ellipse[0], aa_ellipse[1], 'r-', zorder=2, label='AABE')
plt.plot(obb_pts[0,:], obb_pts[1,:], '-k', zorder=2, label='OBB')
plt.plot(o_ellipse[0], o_ellipse[1], 'r-', zorder=2, label='OBE')
plt.title("Step 5: Oriented Bounding Box & Ellipse")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True, zorder=0)
plt.axis('equal')
plt.show()