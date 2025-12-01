import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
print(f"Original Array arr = \n{arr}")

a = arr + 10
print(f"\nAdd 10 to every element: arr + 10 = \n{a}")

a = arr * 3
print(f"\nMultiply 3 by every element: arr * 3 = \n{a}")

a = arr ** 2
print(f"\nRaise every elementy to power of 2: arr ** 2 = \n{a}")

a = np.sqrt(arr)
print(f"\nTake the square root of each element: np.sqrt(arr) = \n{a}")

a = np.log(arr)
print(f"\nTake the log of each element: np.log(arr) = \n{a}")

a = np.sin(arr)
print(f"\nTake the sin of each element: np.sin(arr) = \n{a}")