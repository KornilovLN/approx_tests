#!/bin/python3

####!/usr/bin/env python3

import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from genArr import generator, addNoise

def main():
    # Пример использования
    sizearr = 240
    reduction_factor = 12  # Пример коэффициента прореживания

    # Генерация данных
    data = generator(sizearr)

    # Уменьшение размера данных (прореживание)
    data_small = data[::reduction_factor]

    # Создание кубического сплайна
    x_data_small = np.arange(0, sizearr, reduction_factor) 
    cubic = interp1d(x_data_small, data_small, kind="cubic")

    # Интерполяция на более частом временном интервале (исходном sizearr)
    xh = np.linspace(0, x_data_small[-1], num=sizearr)
    y_cubic = cubic(xh) 
    
    # Визуализация
    fig, ax = plt.subplots(figsize=(24, 6))
    ax.plot(xh, y_cubic, label="Кубический сплайн")
    ax.plot(np.arange(sizearr), data, '.', label="Исходные данные")
    ax.plot(x_data_small, data_small, 'x', label="Прореженные данные")
    ax.legend()
    ax.set_title("Интерполяция кубическим сплайном")
    plt.savefig('spline_transformation.png')
    plt.show()

if __name__ == '__main__':
    main()

