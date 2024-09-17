#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from genArr import generator, addNoise

# Классс для вычисления скользящего среднего
class MovingAverage:
    def __init__(self, window_size):
        self.window_size = window_size
        self.arr_aver = np.zeros(window_size)
        self.pointer = 0
        self.sum = 0
        self.count = 0

    def update(self, dt):
        if self.count < self.window_size:
            self.sum += dt
            self.arr_aver[self.pointer] = dt
            self.count += 1
        else:
            self.sum += dt - self.arr_aver[self.pointer]
            self.arr_aver[self.pointer] = dt

        self.pointer = (self.pointer + 1) % self.window_size
        
        return self.sum / min(self.count, self.window_size)    

def work(sizearr, noise, win_size, reduction_factor):   
    # генерируем массив data
    data = generator(sizearr)
    x = np.arange(sizearr)

    # Зашумляем массив data и получение data_noize
    data_noise = addNoise(data, 100.0, noise)

    # Вычисляем скользящее среднее davg по массиву data_noize
    ma = MovingAverage(win_size)
    davg = []
    for value in data_noise:
        avg = ma.update(value)
        davg.append(avg)
  
    # Уменьшение размера данных (прореживание)
    data_small = davg[::reduction_factor]
    #data_small = data[::reduction_factor]    
    x_data_small = np.arange(0, sizearr, reduction_factor) 

    # Создание кубического сплайна
    cubic = interp1d(x_data_small, data_small, kind="cubic")

    # Интерполяция на более частом временном интервале (исходном sizearr)
    xh = np.linspace(0, x_data_small[-1], num=sizearr)
    y_cubic = cubic(xh) 

    # По всем этим массивам строим графики -------------------------------------------  
    # Графики будут один над другим 3 отдельно и 4-й комбинированый
    # --------------------------------------------------------------------------------
    lb = ('Идеальный массив','Зашумленный массив','Скользящее среднее','Интерполяция')
    dt = [data, data_noise, davg, y_cubic]
    mark = ['.', '.', '.', '*']

    fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(24, 18))

    # Определение общих пределов для оси y
    y_min = min(min(data), min(data_noise), min(davg))
    y_max = max(max(data), max(data_noise), max(davg))

    for i, ax in enumerate(axes):
        if i < 3:
            if i != 0:
                ax.plot(x, dt[i], label=lb[i], linestyle='none', marker=mark[i])
            else:
                ax.plot(x, dt[i], label=lb[i], linestyle='none', marker=mark[i])
            
            if i != 2:
                ax.set_title(lb[i])
            else:    
                ax.set_title(lb[i]+" "+str(win_size))
        else:          
            ax.plot(xh,             dt[3],          label=lb[3]+" "+str(reduction_factor))#, marker=mark[3]) 
            ax.plot(x,              dt[2],          label=lb[2], linestyle='none', marker=mark[2])            
            ax.plot(x_data_small,   data_small, 'o',label="Прореженные данные")
            
            ax.set_title("Combi: "+" "+lb[2]+" точками и "+lb[3]+" сплошной линией")                

        ax.set_ylim(y_min, y_max)           
        ax.set_xlabel('Индекс')
        ax.set_ylabel('Значение')
        ax.legend()
        ax.minorticks_on()
        ax.grid(True)

    fig.tight_layout()
    plt.savefig('combined_plots.png')    
    

# Построение графиков с коефф. зашумления k и окном win
if __name__ == '__main__':    
    k = 0.3
    win = 3
    sizearr = 240
    reduct = 12  # коэффициент прореживания
    work(sizearr, k, win, reduct)                            


    """
    В функции plt.plot() можно использовать маркеры точек графика:
    '.' - точка 
    ',' - пиксель 
    'o' - круг 
    'v' - треугольник вершиной вниз
    '^' - треугольник вершиной вверх 
    '<' - треугольник вершиной влево 
    '>' - треугольник вершиной вправо 
    's' - квадрат 
    'p' - пятиугольник 
    '*' - звезда 
    'h' - шестиугольник1 
    'H' - шестиугольник2 
    '+' - плюс 
    'x' - крест 
    'D' - ромб 
    'd' - тонкий ромб 
    '|' - вертикальная линия 
    '_' - горизонтальная линия

    # Визуализация
    fig, ax = plt.subplots(figsize=(24, 6))
    ax.plot(xh, y_cubic, label="Кубический сплайн")
    ax.plot(np.arange(sizearr), data, '.', label="Исходные данные")
    ax.plot(x_data_small, data_small, 'x', label="Прореженные данные")
    ax.legend()
    ax.set_title("Интерполяция кубическим сплайном")
    plt.savefig('spline_transformation.png')
    plt.show()    
    """