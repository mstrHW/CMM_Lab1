import numpy as np
from algs import euler, euler_cauchy, runge_kutta, adams
import plotly.offline as py
import plotly.figure_factory as ff
import pandas as pd

def plot_answer(X, Y, epsilons, filename = 'answer'):
    df = [['X', 'Y', 'eps']]
    for x, y, eps in zip(X, Y, epsilons):
        df.append([x, y, eps])
    df = pd.DataFrame(columns = df[0], data = df[1:])
    table = ff.create_table(df)
    py.plot(table, filename=filename)

#=====Params=====
h = 0.1
k = 6
X = [round(h * i, 1) for i in range(k)]
y0 = 0.0

f = lambda x, y : (y + x)**2
y_true = lambda x : np.tan(x) - x
epsilon = lambda y_true, y : np.abs(y_true -y)
#=====Params=====


#=====Task1=====
Y, dY = euler(X, y0, h, f)
Y_true = y_true(X)
epsilons = epsilon(Y_true, Y)
plot_answer(X, Y, epsilons, filename='task1.html')
#=====Task1=====


#=====Task2=====
Y, dY = euler_cauchy(X, y0, h, f)
Y_true = y_true(X)
epsilons = epsilon(Y_true, Y)
plot_answer(X, Y, epsilons, filename='task2.html')
#=====Task2=====


#=====Task4=====
Y = runge_kutta(X, y0, h, f)
Y_true = y_true(X)
epsilons = epsilon(Y_true, Y)
plot_answer(X, Y, epsilons, filename='task4.html')
#=====Task4=====


#=====Task5=====
k = 11
X = [round(h * i, 1) for i in range(k)]

Y = adams(X, y0, h, f)
Y_true = y_true(X)
epsilons = epsilon(Y_true, Y)
plot_answer(X, Y, epsilons, filename='task5.html')
#=====Task5=====