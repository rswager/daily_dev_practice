import numpy as np

a = np.array([1, 2, 3]) # From list
print(f"Create Array From a list [1,2,3]:\nnp.array([1,2,3]) = \n{a}")

a = np.zeros((3, 3))    # 3x3 matrix of zeros
print(f"\nCreate a 3x3 matrix of zeros:\nnp.zeros((3, 3)) = \n{a}")

a = np.ones(5)  # 1D array of ones
print(f"\nCreate a 1D array of ones:\nnp.ones(5) = \n{a}")

a = np.arange(0, 10, 2) # Range with step
print(f"\nCreate a 1D array with a Range and step:\nnp.arange(0, 10, 2) = \n{a}")

a = np.linspace(0, 1, 5)    # 5 numbers event spaced between 0 and 1
print(f"\nCreate a 1D 5 evenly spaced numbers:\nnp.linspace(0, 1, 5) = \n{a}")

a = np.eye(4)   # Identity matrix
print(f"\nCreate a 4x4 Identity matrix:\nnp.eye(4) = \n{a}")

a = np.random.rand(2, 3)    # Random 2x3 array (float)
print(f"\nCreate a Random 2x3 array(float):\nnp.random.rand(2, 3) = \n{a}")

a = np.random.randint(low = 4, high =10, size=(2, 3))   # Random 2x3 array (int)
print(f"\nCreate a Random 2x3 array(int):\nnp.random.randint(5, size=(2, 3)) = \n{a}")