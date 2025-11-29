# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 00:34:08 2025

@author: alexa
"""

from saildrone_hydro import get_vals
import base64
import numpy as np

v = np.array([1,0])
theta = np.deg2rad(30)
dtheta = np.deg2rad(0)
beta = np.deg2rad(-5)

force, torque = get_vals(v,theta,dtheta,beta)

print(force)
print(torque)