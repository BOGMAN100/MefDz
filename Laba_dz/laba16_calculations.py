import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
# import os

# print("Текущая рабочая директория:", os.getcwd()) #была проблема в том что рабочая директория была в projects а не в Laba_dz

data1 = pd.read_excel('laba16_data1.xlsx')
data2 = pd.read_excel('laba16_data2.xlsx')

# print(data1)
# print(data2)

# Данные          
X1 = np.array(data1.iloc[1:, 1], dtype='float64') #прямое напряжение
X1 = X1 / 1000

X2 = np.array(data2.iloc[1:, 1], dtype='float64') #обратное напряжение
X2 = np.flip(X2)
X2 = np.append(X2, [0])
X = np.concatenate([X2*-1, X1]) # Ox для ВАХ

Y1 = np.array(data1.iloc[1:,2], dtype='float64') # I прямой

Y2 = np.array(data2.iloc[1:,2], dtype='float64') # I обратный
Y2 = np.flip(Y2)
Y2 = np.append(Y2, [0])
Y3 = np.array(data1.iloc[1:,3], dtype='float64') # ln(I)

Y = np.concatenate([Y2*-1, Y1]) # Oy for BAX

# print(X)
# print(Y)

# Погрешности
# dU = (0.3%*U + 5D)
# dI = (0,008*I + D)
# dLn(I) = sigmaI * ln(I)

def Uerror(u):
    return abs(u*0.003 + 0.05)

def Ierror(i):
    return abs(i*0.008 + 0.1)

dX1 = Uerror(X1)
dX = Uerror(X)

dY1 = Ierror(Y1)
dY = Ierror(Y)
dY3 = Y3 * (dY1/Y1)

# Графики 
f1 = plt.figure(figsize=(14, 10))
plt.errorbar(X, Y, xerr=dX, yerr=0, fmt='o', capsize=5)

# Добавление осей координат
plt.axhline(0, color='black', linewidth=1) # Ось X
plt.axvline(0, color='black', linewidth=1) # Ось Y

# Настройки графика
plt.title('График 1 ВАХ диода')
plt.xlabel('M = 2.5, U, B')
plt.ylabel('M = 2, I, мА')
# plt.legend()

# Настройка сетки
plt.grid(which='major', color='gray', linestyle='-', linewidth=0.5)  # Основная сетка с интервалом разбиения
plt.grid(which='minor', color='gray', linestyle=':', linewidth=0.5)  # Дополнительная сетка

# Установка основных и дополнительных делений
plt.minorticks_on()
plt.xticks(np.arange(-5, 1, 0.25))
plt.yticks(np.arange(-140, 200, 20))
plt.gca().set_xticks(np.arange(-5, 1, 0.025), minor=True)
plt.gca().set_yticks(np.arange(-140, 200, 2), minor=True)
plt.tick_params( which='both', direction='in')
plt.xlim([-5, 1])
plt.ylim([-140, 200])


plt.plot(X, Y)
plt.show()

# Создание нового графика
f2 = plt.figure(figsize=(14, 10))

plt.errorbar(X1, Y3, xerr=dX1/10, yerr=dY3, fmt='o', capsize=5)

# Добавление осей координат
plt.axhline(0, color='black', linewidth=1) # Ось X
plt.axvline(0, color='black', linewidth=1) # Ось Y

# Настройки графика
plt.title('График 1 зависимости ln(I) от U')
plt.xlabel('M= 2, U, B')
plt.ylabel('M= 2, ln(I), мА')
# plt.legend()

# Настройка сетки
plt.grid(which='major', color='gray', linestyle='-', linewidth=0.5)  # Основная сетка с интервалом разбиения
plt.grid(which='minor', color='gray', linestyle=':', linewidth=0.5)  # Дополнительная сетка

# Установка основных и дополнительных делений
plt.minorticks_on()
plt.xticks(np.arange(0.500, 0.800, 0.020))
plt.yticks(np.arange(2.4, 5.6, 0.2))
plt.gca().set_xticks(np.arange(0.500, 0.800, 0.0020), minor=True)
plt.gca().set_yticks(np.arange(2.4, 5.6, 0.02), minor=True)
plt.tick_params( which='both', direction='in')
plt.xlim([0.500, 0.800])
plt.ylim([2.4, 5.6])

equasion = np.polyfit(X1, Y3, 1)
# print(equasion)
plt.plot(X1, X1*equasion[0] + equasion[1])

# Вывод

# print(dX)

# print(dY3)

# print(dY)

print(f'k = {equasion[0]}, b = {equasion[1]}')

plt.show()