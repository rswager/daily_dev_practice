import numpy as np

a = np.array([[1, 2],
              [3, 4]])
print(f"Original Array a = \n{a}")

b = np.array([[5, 6],
              [7, 8]])
print(f"\nOriginal Array b = \n{b}")

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])
print(f"\nOriginal Array matrix = \n{matrix}")

arr = np.array([10, 20, 30, 40, 50, 60])
print(f"\nOriginal Array arr = \n{arr}")

c = np.concatenate([a, b], axis=0)     # stack rows
print(f"\nstack rows of a,b: np.concatenate([a, b], axis=0) = \n{c}")

c = np.vstack([a, b])                  # vertical stack
print(f"\nvertically stack a,b: np.vstack([a, b])  = \n{c}")

c = np.hstack([a, b])                  # horizontal stack
print(f"\nhorizontally stack a,b: np.hstack([a, b])   = \n{c}")

c = np.stack([a,b], axis=0)            # preserves new dimension [a, b]
print(f"\nstack a,b and preserve new dimension: preserves new dimension = \n{c}")

c = np.split(arr, 3)               # split 1D array
print(f"\nsplit 1D array into 3 pieces: np.split(arr, 3)  = \n{c}")

c = np.hsplit(matrix, 2)               # split columns
print(f"\nsplit matrix array into 2 pieces: np.hsplit(matrix, 2)   = \n{c}")

c = np.vsplit(matrix, 2)               # split rows
print(f"\nsplit matrix array into 2 pieces: np.vsplit(matrix, 2)  = \n{c}")
