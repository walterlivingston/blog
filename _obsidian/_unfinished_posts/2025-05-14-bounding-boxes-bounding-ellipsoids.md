---
layout: post
title: Bounding Boxes & Bounding Ellipsoids
date: 2025-05-14 14:52:59
categories:
  - blog
tags:
  - sensor-fusion
  - kalman-filter
  - bounding
  - aabb
  - obb
  - obe
comments: true
---
## Introduction
Bounding geometries for a set of points can be very useful in fields such as robotics and autonomous vehicles. They can also be applied to some niche fields such as geometrically bounding covariance matrices.[^1] They can be difficult to create, that is, unless you know a few tricks.
## Overview
The majority of the bounding box creation was originally defined by Sai Sharath Kakubal in his article "2D Oriented bounding boxes made simple".[^2] For consistencies sake, a lot of this will be redefined in this article, with the addition of bounding ellipsoids. The steps of this process are as follows:
1. Obtain Sample Data
2. Principal Component Analysis
3. Rotate the Data to be Axis-Aligned
4. Form Axis-Aligned Bounding Box (AABB) & Axis-Aligned Bounding Ellipse
5. Form Oriented Bounding Box (OBB) & Oriented Bounding Ellipse (OBE)
### Step 1: Obtain Sample Data
The first step to this process is obtaining sample data. In application, this may be obtained in various ways. The data may be point clouds or sampled ellipses, but for our example here we will generate random points to act as our sampled data. Arbitrary biases and standard deviations were added to the data to make it realistic to actual applications. A rotation to the data was also added.
```python
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
[np.sin(theta), np.cos(theta)]])
rot_data = R @ data
```
### Step 2: Principal Component Analysis
COME BACK AND ADD IN DEPTH PCA DEFINITION
```python
# principal component analysis
P = np.cov(rot_data)
mu = np.mean(rot_data, axis=1)
centered_data = np.transpose(rot_data.T - mu)
D, V = np.linalg.eig(P.T)
```
### Step 3: Rotate the Data to be Axis-Aligned
Utilizing the eigenvector matrix obtained through PCA, the centered data can be rotated to be axis-aligned.
```python
# axis-align data
aa_points = V.T @ centered_data
```
### Step 4: Form Axis-Aligned Bounding Box (AABB) & Axis-Aligned Bounding Ellipse (AABE)
With the data axis-aligned, it is trivial to form a bounding box around it. This is done by finding the maximum and minimum x and y values of the data. These are then subtracted to get the size of the box; i.e. width and height. Using these values, the corner points of the bounding box can be formed.
```python
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
```
### Step 5: Form Oriented Bounding Box (OBB) & Oriented Bounding Ellipse (OBE)
Converting the axis-aligned bounding box (AABB) to an oriented bounding box is very simple. The corner points calculated in Step 3 need to be rotated back to the original frame using the eigenvectors obtained through PCA in Step 1.
Converting this oriented bounding box in
```python
# oriented bounding box
obb_pts = V @ pts
obb_pts = np.transpose(obb_pts.T + mu)

# oriented bounding ellipse
tolerance = 1
eigenvalues = ((np.sqrt(2 + (tolerance*2))/(sz))**2)
S_aabe = np.diag(eigenvalues)
S_obe = np.diag(eigenvalues)
```
## Applications
For my personal research, these bounding geometries were used to geometrically define the innovation covariance of a Kalman filter. This was done by sampling the points for the state and measurement error ellipses, and performing the above calculations to create a bounding ellipse(or in my case ellipsoid) around these error ellipses in order to form a better innovation covariance than the typical Kalman filtering equations. My paper on the topic is "Pedestrian Attitude Estimation using a Multiplicative Extended Kalman Filter with Geometrically-Defined Innovation Covariance"[^1].
## Conclusions
## Future Work

## References
[^1]: My paper 
[^2]: https://logicatcore.github.io/scratchpad/lidar/sensor-fusion/jupyter/2021/04/20/2D-Oriented-Bounding-Box.html