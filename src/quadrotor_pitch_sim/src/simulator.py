import numpy as np
from scipy.integrate import solve_ivp

def pid_controller(setpoint, theta, omega, kp, ki, kd, integral, dt):
    error = setpoint - theta
    integral += error * dt
    derivative = -omega
    torque = kp * error + ki * integral + kd * derivative
    return torque, integral

def closed_loop_dynamics(t, state, setpoint, kp, ki, kd, I):
    theta, omega = state
    dt = 0.01  # Дискретизация по времени, может быть адаптирована
    integral = 0.0  # Инициализация интеграла

    torque, integral = pid_controller(setpoint, theta, omega, kp, ki, kd, integral, dt)

    dtheta_dt = omega
    domega_dt = torque / I

    return [dtheta_dt, domega_dt]

def simulate(I, torque_coefficient, setpoint, initial_conditions, t_span, t_eval):
    kp, ki, kd = torque_coefficient, 0.1, 0.01  # Пример значений PID коэффициентов

    # Лямбда-функция для передачи параметров в dynamics
    closed_loop_dynamics_with_params = lambda t, y: closed_loop_dynamics(t, y, setpoint, kp, ki, kd, I)

    # Решение системы уравнений с использованием метода интеграции
    sol = solve_ivp(closed_loop_dynamics_with_params, t_span, initial_conditions, t_eval=t_eval)

    return sol
