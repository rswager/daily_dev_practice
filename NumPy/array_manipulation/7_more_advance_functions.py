import numpy as np


a = np.array([1,2,3])
print(f"Original Array: a = \n{a}")
b = np.array([[10],[20],[30]])
print(f"\nOriginal Array: b = \n{b}")

c = a + b       # automatic expansion
print(f"\nSum Arrays:a + b = \n{c}")


A = np.array([[2, 1],
              [3, 4]])
print(f"\nOriginal Array: A = \n{A}")

c = np.dot(a, b)                  # dot product
print(f"\nDot Production of Arrays: np.dot(a, b) = \n{c}")

c = np.matmul(a, b)               # matrix multiplication
print(f"\nMatrix Multiplication of Arrays: np.matmul(a, b)  = \n{c}")
c = np.linalg.inv(A)              # inverse
print(f"\nInverse of array: A = \n{c}")
c = np.linalg.det(A)              # determinant
print(f"\nDeterminant of array: A = \n{c}")
c = np.linalg.eig(A)              # eigenvalues/vectors
print(f"\nEigenvalues/Vectors of array: A = \n{c}")

