import numpy as np

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

# Пример использования
if __name__ == "__main__":
    A = np.array([[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]], dtype=float)
    
    b = np.array([[8],
                  [-11],
                  [-3]], dtype=float)
    
    xes = np.array([1,3,4,6])

    wow = np.array(list(map(lambda x : x**2, xes)))
    print(wow)

    solution = cramers_rule(A, b)
    print("Решение системы уравнений:", solution)   