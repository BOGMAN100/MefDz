import numpy as np
import matplotlib.pyplot as plt

# np.linalg.solve()

n = 20

data_x = np.linspace(0, 26, n)

data_y = np.array([(1+i**2) for i in data_x])

# coefs = np.polyfit(data_x, data_y, 2)

# print(coefs)
                                                    #  читы(
# p=np.poly1d(coefs)

# x=np.linspace(data_x.min(), data_x.max())

# y=p(x)

# plt.plot(data_x, data_y, "o", x, y)

# plt.show()

# знаем что функция квадратичная
systx = np.arange(9)
systy = np.arange(3)
syst_x = systx.reshape(3,-1,3)
syst_y = systy.reshape(1,-1,3)

syst_x = syst_x.reshape(-1,3)      # костылю немного
syst_y = syst_y.reshape(-1, 1)

# print(syst_x, "\n")
# print(syst_y)


#да, я не хотел сам его писать
def cramers_rule(A, b):   


    # Проверяем, что A квадратная матрица
    if A.shape[0] != A.shape[1]:
        raise ValueError("Матрица A должна быть квадратной.")
    
    # Проверяем, что размерности A и b совместимы
    if A.shape[0] != b.shape[0]:
        raise ValueError("Размерности матрицы A и вектора b несовместимы.")

    # Вычисляем детерминант матрицы A
    det_A = np.linalg.det(A)
    
    # Если детерминант равен нулю, система не имеет единственного решения
    if det_A == 0:
        raise ValueError("Детерминант матрицы A равен нулю. Система не имеет единственного решения.")
    
    # Количество переменных
    n = A.shape[0]
    
    # Инициализируем вектор решения
    x = np.zeros(n)
    
    # Вычисляем решения по методу Крамера
    for i in range(n):
        # Создаем матрицу Ai, заменяя i-ый столбец A на b
        Ai = A.copy()
        Ai[:, i] = b.flatten()
        
        # Вычисляем детерминант матрицы Ai
        det_Ai = np.linalg.det(Ai)
        
        # Находим i-ый элемент решения
        x[i] = det_Ai / det_A
    
    return x

# рассчет и заполнение syst_x (sum(x**k+l))

for i in range(3):  
    for j in range(3):
        
        B = np.array(list(map(lambda x : x**(i+j), data_x)))
        # print(B)
        c = sum(B)
        # print(c)
        syst_x[i][j] = c

# print(syst_x)
# заполнение syst_y (sum(x**k * y))

for k in range(3):
    B2 = np.array(list(map(lambda x : x**k, data_x))) #массив с x^k
    Y = data_y*B2
    b = sum(Y)
    syst_y[k][0] = b

solution = cramers_rule(syst_x, syst_y)
print("Решение системы уравнений:", solution) #коэффициенты

p = np.poly1d(solution)  #функция многочлен с полученными коэффициентами
# print(p)
my_data_y = p(data_x)
plt.scatter(data_x, data_y, label = "точки")

plt.plot(data_x, my_data_y, color = "red")

plt.show()


