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
---

# Bounding Boxes & Bounding Ellipsoids
## Introduction
Bounding geometries for a set of points can be very useful in fields such as robotics and autonomous vehicles. They can also be applied to some niche fields such as geometrically bounding covariance matrices.[^1] They can be difficult to create, that is unless you know a few tricks.
## Overview
The majority of the bounding box creation was original defined Sai Sharath Kakubal in his article "2D Oriented bounding boxes made simple".[^2] For consistencies sake, a lot of this will be redefined in this article, with the addition of bounding ellipsoids. The steps of this process are as follows:
1. Subtract the Mean of the Data
2. Rotate the Data to be Axis-Aligned
3. Form an Axis-Aligned Bounding Box (AABB)
4. Convert Oriented Bounding Box (OBB) to Oriented Bounding Ellipse (OBE)
5. Rotate the Data Back
6. Add Back the Mean
### Subtract the Mean of the Data
### Rotate the Data to be Axis-Aligned
### Form an Axis-Aligned Bounding Box (AABB)
### Convert Oriented Bounding Box (OBB) to Oriented Bounding Ellipse (OBE)
### Rotate the Data Back
### Add Back the Mean
## Applications
For my personal research, these bounding geometries were used to geometrically define the innovation covariance of a Kalman filter. This was done by sampling the points for the state and measurement error ellipses, and performing the above calculations to create a bounding ellipse(or in my case ellipsoid) around these error ellipses in order to form a better innovation covariance than the typical Kalman filtering equations. My paper on the topic is "Pedestrian Attitude Estimation using a Multiplicative Extended Kalman Filter with Geometrically-Defined Innovation Covariance"[^1].
## Conclusions
## Future Work

## References
[^1]: My paper 
[^2]: https://logicatcore.github.io/scratchpad/lidar/sensor-fusion/jupyter/2021/04/20/2D-Oriented-Bounding-Box.html