import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])
print(f"Original Array:\n{arr}")

#💡 reshape() allows changing structure as long as total elements match.
a=arr.reshape(3, 4)                  # Change shape (same # of elements)
print(f"\nReshape Original array to be 3x4 instead of 4x3:\narr.reshape(3, 4) = \n{a}")

try:
    a = arr.reshape(3,5)
    print(f"\nReshape Original array to be 3x5 instead of 4x3:\narr.reshape(3, 5) = \n{a}")
except:
    print(f"\nReshape Original array to be 3x5 instead of 4x3:\narr.reshape(3, 5) = \nFAILURE required 15 elements only found 12")


a=arr.ravel()                        # Flatten (view) as 1-D -> returns a reference to the original array
print(f"\nFlatten Original Array to 1-D (give reference back):\narr.ravel() = \n{a}")

a=arr.flatten()                      # Flatten (copy) as 1-D -> returns a copy of the original array not a reference
print(f"\nFlatten Original Array to 1-D (give copy back):\narr.flatten()  = \n{a}")

a=arr.T                              # Transpose
print(f"\nTranspose the Original Array:\narr.T = \n{a}")

a=arr.reshape(-1, 6)                 # Let NumPy infer dimension
print(f"\nReshape the Original Array, but let NumPy infer dimension:\narr.reshape(-1, 6) = \n{a}")

a=arr.reshape(-1, 2)                 # Let NumPy infer dimension
print(f"\nReshape the Original Array, but let NumPy infer dimension:\narr.reshape(-1, 2) = \n{a}")