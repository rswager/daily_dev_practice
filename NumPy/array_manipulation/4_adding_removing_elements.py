import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
print(f"Original Array arr = \n{arr}")

a = np.append(arr, [99]) # add to end (returns copy)
print(f"\nappend to end (returns copy): np.append(arr, [99]) = \n{a}")

a = np.insert(arr, 2, [5,6]) # insert at index
print(f"\ninsert at index: np.insert(arr, 2, [5,6]) = \n{a}")

a = np.delete(arr, [1,4]) # remove by index
print(f"\nremove at index: np.delete(arr, [1,4]) = \n{a}")