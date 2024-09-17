#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt

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

def work():
    win_size = 5

    # Пример использования
    ma = MovingAverage(win_size)
    data = [1.0, 1.9, 1.4, 1.9, 1.2, 1.3, 1.4, 7.1, 3.5, 1.7, 1.7, 1.1, 1.4, 1.5, 1.2, 1.8, 1.3, 1.4, 1.1]
    davg = []

    for value in data:
        avg = ma.update(value)
        davg.append(avg)
        print(f"{avg:.2f} {value:.2f}")


    # Создание графика
    plt.figure(figsize=(12, 6))
    plt.plot(data, label='Исходный массив', marker='o')
    plt.plot(davg, label='Скользящее среднее', marker='s')
    plt.title('Исходный массив и скользящее среднее')
    plt.xlabel('Индекс')
    plt.ylabel('Значение')
    plt.legend()
    plt.grid(True)
    plt.savefig('moving_average_plot.png')
    #plt.show()    

work()                            
