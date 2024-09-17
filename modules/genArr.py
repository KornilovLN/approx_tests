#!/bin/python3

import math
import numpy as np
import pandas as pd

NUMB = 240 #1000
PI2 = 2*math.pi
PIdiv2 = PI2/2

am = np.array([1000.0, PIdiv2, 0.0], dtype=float)
frq = np.array([1, 1.2, 0.0], dtype=float)
phs = np.array([0.0, 0.0, 0.0], dtype=float)

def genFunc(ampl, freq, phase, t):
    arg = PI2*freq*t + phase
    return ampl*math.sin(arg)    

def genAmpl(ampl, freq, phase, t):
    arg = PI2*freq*t + phase
    return ampl*np.sin(arg)

def genFreq(ampl, freq, phase, t):
    arg = PI2*freq*t + phase
    return ampl*np.sin(arg)

def genPhase(ampl, freq, phase, t):
    arg = PI2*freq*t + phase
    return ampl*np.sin(arg)

def generator(numb):
    arr = []
    t = 0
    dt = 1.0/numb
    for i in range(numb):
        #t += i/numb  
        t += dt     

        ampl = genAmpl(am[0], am[1], am[2], 0.3)
        freq = genFreq(frq[0], frq[1], frq[2], t)
        phase = genPhase(phs[0], phs[1], phs[2], t)
        arr.append(genFunc(ampl, freq, phase, t))
    return arr

def addNoise(arr, diapason, max_noize):
    arres = []
    for val in arr:
        rnd = np.random.normal(0, max_noize)
        #arres.append(val + rnd*val)
        arres.append(val + rnd*diapason)
    return arres

def outArr(arr, n):
    for i, val in enumerate(arr):
        formatted_val = f"{val:7.2f}".replace("+", " ").replace("0 ", "  ")
        print(formatted_val, end=" ")
        if (i + 1) % n == 0:
            print()
    if len(arr) % n != 0:
        print()

def work_GenOut(n_str):
    genArr = generator(NUMB)
    outArr(genArr, n_str)

def main():
    work_GenOut(20)
                    
if __name__ == '__main__':
    main()