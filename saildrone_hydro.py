"""
This module provides an interface to hydropdynamic measurements of a sail drone 
collected experimentally in a flow tank.

Author: Alan Hunter
Date: 2025-10
"""

__all__ = ['get_vals']

import base64
import numpy as np


# Data file containing compressed measurements
FILENAME = 'saildrone_hydro.dat'


# Import data
_data = open(FILENAME,"r").read()
exec(base64.b64decode(_data).decode('utf-8'))


def get_vals(velocity,heading,turn_rate,rudder_angle):
    """
    Get hydrodynamic force and torque values by interpolating meeasurement data.
    
    Parameters
    ----------
    velocity : ndarray
        2-D velocity of the sail drone in m/s.
    heading : float
        drone orientation in rad. Angles are positive in the anti-clockwise 
        direction relative to the positive x axis.
    turn_rate : float
        turning rate in rad/s.
    rudder_angle : float
        Rudder deflection angle in rad.

    Returns
    -------
    force : np.array
        Resultant 2-D force vector in N.
    torque : float64
        Resultant torque in Nm.
    """
    
    force, torque = _eval_data(velocity,heading,turn_rate,rudder_angle)
    
    return force, torque


if __name__ == '__main__':
    # Test code
    
    v = np.array([1,0])
    theta = np.deg2rad(30)
    dtheta = np.deg2rad(0)
    beta = np.deg2rad(-5)
    
    print('----')
    print(f'Velocity = [{v[0]:.2f}, {v[1]:.2f}] m/s')
    print(f'Heading = {np.rad2deg(theta):.1f} deg')
    print(f'Turn rate = {np.rad2deg(dtheta):.2f} deg/s')
    print(f'Rudder angle = {np.rad2deg(beta):.2f} deg')

    force, torque = get_vals(v,theta,dtheta,beta)
    
    print('----')
    print(f'Hydrodynamic force = [{force[0]:.0f}, {force[1]:.0f}] N')
    print(f'Hydrodynamic torque = {torque:.0f} N.m')
    print('----')