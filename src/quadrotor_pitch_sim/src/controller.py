def pid_controller(setpoint, current_position, current_velocity, kp, ki, kd, integral, dt):
    error = setpoint - current_position
    integral += error * dt
    derivative = current_velocity / dt
    control_signal = kp * error + ki * integral - kd * derivative
    return control_signal, integral
