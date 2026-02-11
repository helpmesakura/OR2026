import numpy as np
from scipy.optimize import linprog


def solve_task_2():
    N = 11
    num_vars = 10 * N

    c = np.zeros(num_vars)
    A_ub = []
    b_ub = []

    for k in range(num_vars - 2):
        row = np.zeros(num_vars)
        row[k] = 1
        row[k + 1] = 2
        row[k + 2] = -1
        A_ub.append(row)
        b_ub.append(100)

    A_eq = [np.ones(num_vars)]
    b_eq = [200]

    bounds = [(0, None) for _ in range(num_vars)]

    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    if res.success:
        sum_x = 200
        min_sum_y = 0
        result = sum_x - N * min_sum_y
        print(f"Система ограничений для x совместна.")
        print(f"Оптимальное значение всех y_ij = 0.")
        print(f"Целевая функция: {sum_x} - {N} * 0")
        print(f"Ответ: {result}")
    else:
        print("Система ограничений не имеет решений.")


if __name__ == "__main__":
    solve_task_2()