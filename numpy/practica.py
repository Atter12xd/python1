import numpy as np

arr_1d = np.array([10, 20, 30])
print(arr_1d)

arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
result = arr_1d + arr_2d
print(result)


arr = np.array([10, 20, 30, 40, 50])
sliced = arr[1:4]  # Obtiene [20, 30, 40]
print(sliced)