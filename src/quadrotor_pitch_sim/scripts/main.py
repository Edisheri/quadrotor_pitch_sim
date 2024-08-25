#!/usr/bin/env python3

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import yaml
from simulator import simulate
from plotter import plot_results

def main():
    with open(os.path.join(os.path.dirname(__file__), '../config/config.yaml'), 'r') as file:
        config = yaml.safe_load(file)

    I = config['I']
    torque_coefficient = config['torque_coefficient']
    setpoint = config['setpoint']
    initial_conditions = config['initial_conditions']
    t_span = config['t_span']
    t_eval = config['t_eval']

    result = simulate(I, torque_coefficient, setpoint, initial_conditions, t_span, t_eval)

    plot_results(result.t, result.y[0], result.y[1])

if __name__ == "__main__":
    main()
