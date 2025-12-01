import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
print(f"Original Array: arr = \n{arr}")
arr2d = np.array([[10, 20, 30], [40, 50, 60]])
print(f"\nOriginal Array: arr2d = \n{arr2d}")


a = arr.sum()
print(f"\nSum elements of array: arr.sum() = \n{a}")
a = arr2d.sum()
print(f"\nSum elements of 2d array: arr2d.sum() = \n{a}")

a = arr.mean()
print(f"\nCalculate the means of the elements in the array: arr.sum() = \n{a}")
a = arr2d.mean()
print(f"\nCalculate the means of the elements in the 2D array: arr2d.sum() = \n{a}")

a = arr.std()
print(f"\nCalculate the std deviations of the elements in the array: arr.sum() = \n{a}")
a = arr2d.std()
print(f"\nCalculate the std deviations of the elements in the 2D array: arr2d.sum() = \n{a}")

a,b = arr.min(), arr.max()
print(f"\nCalculate min/max of an array: arr.min(), arr.max() = \n{a},{b}")
a,b = arr2d.min(), arr2d.max()
print(f"\nCalculate min/max of a 2D array: arr2d.min(), arr2d.max() = \n{a},{b}")

a,b = arr.argmin(), arr.argmax()
print(f"\nCalculate the index of the min/max of an array: arr.argmin(), arr.argmax() = \n{a},{b}")
a,b = arr2d.argmin(), arr2d.argmax()
print("\n2D arrays will be flattened")
print(f"Calculate the index of the min/max of a 2d array: arr2d.argmin(), arr2d.argmax() = \n{a},{b}")

a = np.percentile(arr, 90)
print(f"\nCalculate percentage of values below 90: np.percentile(arr, 90) = \n{a}")
a = np.percentile(arr2d, 90)
print(f"\nCalculate percentage of values below 90: np.percentile(arr2d, 90) = \n{a}")


"""Also supports operations across specific axes:"""
arr2d.sum(axis=0)   # column-wise sum
arr2d.sum(axis=1)   # row-wise sum
