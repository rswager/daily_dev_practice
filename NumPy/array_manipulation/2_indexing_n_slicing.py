import numpy as np

"""
Basic Slice Format
    start : stop : step

| Part    | Meaning                      | Default if omitted |
| ------- | ---------------------------- | ------------------ |
| `start` | Starting index (inclusive)   | `0`                |
| `stop`  | Ending index (**exclusive**) | End of array       |
| `step`  | How much to move each time   | `1`                |

arr = np.array([[10,20,30],
                [40,50,60]])

Examples
| Code            | Meaning                           | Result              |
| --------------- | --------------------------------- | ------------------- |
| `arr[0:2, 0:2]` | rows 0→2 (0,1) and cols 0→2 (0,1) | `[[10,20],[40,50]]` |
| `arr[:, 0:2]`   | **all rows**, first 2 columns     | `[[10,20],[40,50]]` |
| `arr[1:, :]`    | last row to end, **all cols**     | `[[40,50,60]]`      |
| `arr[-2:, -2:]` | last 2 rows + last 2 columns      | `[[20,30],[50,60]]` |


Negative Slicing
| Code          | Meaning        |
| ------------- | -------------- |
| `arr[-1]`     | last row       |
| `arr[-2:]`    | last 2 rows    |
| `arr[:, -1]`  | last column    |
| `arr[:, -2:]` | last 2 columns |


Reversing
| Slice             | Effect                                    |
| ----------------- | ----------------------------------------- |
| `arr[::-1]`       | Reverse rows (flip vertically)            |
| `arr[:, ::-1]`    | Reverse columns (flip horizontally)       |
| `arr[::-1, ::-1]` | Reverse both rows + columns (rotate 180°) |


| Method         | Meaning                        |
| -------------- | ------------------------------ |
| slicing        | take ranges `[start:end:step]` |
| boolean mask   | filter based on condition      |
| fancy indexing | pass list of indices           |

"""


arr = np.array([[10,20,30],[40,50,60]])
print(f"Original Array = \n{arr}")

a=arr[0,1]        # element at row0 col1 → 20
print(f"\nreturn Element at row 0 col 1:\narr[0,1] = \n{a}")

a=arr[:,1]        # column 1 -> [20,50]
print(f"\nReturn column 1:\narr[:,1] = \n{a}")

a=arr[1,:]        # row 1 -> [40,50,60]
print(f"\nReturn row 1:\narr[1,:] = \n{a}")

a=arr[0:2,0:2]    # sub-array slicing
print(f"\nReturn Rows 0,1 for column 0,1:\narr[0:2,0:2] = \n{a}")

a=arr[-2:,-2:]    # sub-array slicing
print(f"\nReturn last 2 rows for last two columns:\narr[-2:,-2:] = \n{a}")

a=arr[arr > 30]     # boolean mask → [40,50,60]
print(f"\nReturn where value > 30:\narr[arr > 30]  = \n{a}")

a=arr[arr%20 == 0]     # boolean mask → [20,40,60]
print(f"\nReturn where value is a factor of 20:\narr[arr%20 == 0] = \n{a}")

a=arr[::-1] # Reverse rows (flip vertically)
print(f"\nReverse rows(flip vertically):\narr[::-1] = \n{a}")

a=arr[:, ::-1] # Reverse columns (flip horizontally)
print(f"\nReverse columns (flip horizontally):\narr[:, ::-1] = \n{a}")

a=arr[::-1,::-1] # Reverse columns and rows (flip 180 degrees) (FASTER AND GIVES REFERENCE)
print(f"\nReverse columns and rows (flip 180 degrees):\narr[::-1,::-1] = \n{a}")

a=arr.flatten()[::-1].reshape(2,3)  #another way to flipt 180 degrees (SLOWER AND A COPY)
print(f"\nAnother way to reverse columns and rows (flip 180 degrees):\narr.flatten()[::-1].reshape(2,3) = \n{a}")