import numpy as np

def rotational_dynamics(t, y, I, torque):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = torque / I
    return [dtheta_dt, domega_dt]
