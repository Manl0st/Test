import numpy as np

def solve_system(A, b):
    n = A.shape[0]
    det_A = np.linalg.det(A)
    if det_A == 0:
        raise ValueError("Определитель матрицы A равен 0, система не имеет единого решения")
    solution = np.zeros(n, dtype=complex)
    for i in range(n):
        A_copy = A.copy()
        A_copy[:, i] = b
        det_A_i = np.linalg.det(A_copy)
        solution[i] = det_A_i / det_A
    return solution

A = np.array([[3, 7], [3, 2]], dtype=complex)
b = np.array([6, 5], dtype=complex)
print("\nОтвет:")
x = solve_system(A, b)
for i in range(len(x)):
    print(f"x{i+1} = {x[i]:.2f}")