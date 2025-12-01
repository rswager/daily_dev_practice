from left_right_problem import front_back_given_index, right_left_given_index
import numpy as np
import math

center = np.array([0,0])

P_counter_clock_wise_unit_circle = np.array([
    [1,0],  [math.sqrt(3)/2, 1/2],     [math.sqrt(2)/2, math.sqrt(2)/2],    [1/2, math.sqrt(3)/2],
    [0,1],  [-1/2,math.sqrt(3)/2],    [-math.sqrt(2)/2,math.sqrt(2)/2],   [-math.sqrt(3)/2,1/2],
    [-1,0], [-math.sqrt(3)/2,-1/2],   [-math.sqrt(2)/2,-math.sqrt(2)/2],  [-1/2, -math.sqrt(3)/2],
    [0,-1], [1/2, -math.sqrt(3)/2],   [math.sqrt(2)/2,-math.sqrt(2)/2],   [math.sqrt(3)/2,-1/2]
])
print("Counter Clock Wise Unit Circle")
print("\t[", end = '')
for index,data in enumerate(P_counter_clock_wise_unit_circle):
    if index < len(P_counter_clock_wise_unit_circle)-1:
        result = right_left_given_index(P=P_counter_clock_wise_unit_circle,i=index,sign_loc=center)
        print(f"({index},{result})", end=' ')
        assert result == 'LEFT'
print("]")

print("\nClock Wise Unit Circle")
P_clockwise_unit_circle = P_counter_clock_wise_unit_circle[::-1]
print("\t[", end = '')
for index,data in enumerate(P_clockwise_unit_circle):
    if index < len(P_clockwise_unit_circle)-1:
        result = right_left_given_index(P=P_clockwise_unit_circle,i=index,sign_loc=center)
        print(f"({index},{result})", end=' ')
        assert result == 'RIGHT'
print("]")