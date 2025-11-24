import numpy as np

# NOTE(rswager): TLDR here is the solutions
def front_back_given_index(P,i,sign_loc):
    return 'FRONT' if np.dot(((P[i+1] - P[i])/np.linalg.norm(P[i+1] - P[i])), sign_loc-P[i])>0 else 'BACK'

def right_left_given_index(P,i,sign_loc):
    dp_unit_vector = (P[i+1] - P[i])/np.linalg.norm(P[i+1] - P[i])
    return 'RIGHT' if np.dot(np.array([dp_unit_vector[1],-dp_unit_vector[0]]),np.array(sign_loc-P[i]))>0 else 'LEFT'


left_sign = np.array([-1.0, 1.0])
right_sign = np.array([1.0, 1.0])

P = np.array([
        [0.0, 0.0], #P0
        [0.0, 2.0], #P1
        [0.0, 4.0]  #P2
    ])
print('''
4 _|__|__|__|__|__|P2|__|__|__|__|__|
3 _|__|__|__|__|__|__|__|__|__|__|__|
2 _|__|__|__|__|__|P1|__|__|__|__|__|
1 _|__|__|__|__|L |__| R|__|__|__|__|
0 _|__|__|__|__|__|P0|__|__|__|__|__|
    -5 -4 -3 -2 -1  0  1  2  3  4  5
''')

print(f"left_sign = {right_left_given_index(P,0,left_sign)}")
print(f"left_sign = {front_back_given_index(P,0,left_sign)}")
print(f"right_sign = {right_left_given_index(P,0,right_sign)}")
print(f"right_sign = {front_back_given_index(P,0,right_sign)}")

print("\nFLIP P")
print('''
4 _|__|__|__|__|__|P0|__|__|__|__|__|
3 _|__|__|__|__|__|__|__|__|__|__|__|
2 _|__|__|__|__|__|P1|__|__|__|__|__|
1 _|__|__|__|__|L |__| R|__|__|__|__|
0 _|__|__|__|__|__|P2|__|__|__|__|__|
    -5 -4 -3 -2 -1  0  1  2  3  4  5
''')
# let's make P point the other way
P = np.array([
        [0.0, 4.0], #P0
        [0.0, 2.0], #P1
        [0.0, 0]  #P2
    ])

print(f"left_sign = {right_left_given_index(P,1,left_sign)}")
print(f"left_sign = {front_back_given_index(P,1,left_sign)}")
print(f"right_sign = {right_left_given_index(P,1,right_sign)}")
print(f"right_sign = {front_back_given_index(P,1,right_sign)}")

quit()
print("WORKING STUFF \n")
# NOTE(rswager): Work I stepped through to find solution
# NOTE(rswager): for the purpose of this we can assume we are in ENU and in 2D
print('''
4 _|__|__|__|__|__|P2|__|__|__|__|__|
3 _|__|__|__|__|__|__|__|__|__|__|__|
2 _|__|__|__|__|__|P1|__|__|__|__|__|
1 _|__|__|__|__|L |__| R|__|__|__|__|
0 _|__|__|__|__|__|P0|__|__|__|__|__|
    -5 -4 -3 -2 -1  0  1  2  3  4  5
''')
left_sign = np.array([-1.0, 1.0])
right_sign = np.array([1.0, 1.0])

P = np.array([
        [0.0, 0.0], #P0
        [0.0, 2.0], #P1
        [0.0, 4.0]  #P2
    ])

print(f"{P=}\n")
# Compute Segment Vectors: P[i+1]-P[i]
dP = P[1:] - P[:-1]
print(f"{dP=}\n")

# Compute Length of each Segment
dP_norm = np.linalg.norm(dP, axis=1)
print(f"{dP_norm=}\n")

print(f"{dP_norm.shape=}\n")
print(f"{dP_norm[:,None].shape=}\n")

# Compute Unit Vectors:
dP_unit_vectors = dP/dP_norm[:,None]
print(f"{dP_unit_vectors=}\n")

# Right Orthogonal
n_unit_vector = np.column_stack((dP_unit_vectors[:,1], -dP_unit_vectors[:,0]))
print(f"{n_unit_vector=}\n")

# Dot Product with orthogonal vector ni  to get left/right -> value<0 Left, value<ni Right
ni_left_sign    = np.einsum('ij,ij->i',n_unit_vector,left_sign-P[:-1])
print(f"{ni_left_sign=}")
ni_right_sign   = np.einsum('ij,ij->i',n_unit_vector,right_sign-P[:-1])
print(f"{ni_right_sign=}")

# Dot Product with unit vector dP_unit_vectors to get in_front/behind -> value>0 in_front, value<0 behind
dP_unit_vectors_left_sign   = np.einsum('ij,ij->i',dP_unit_vectors, left_sign-P[:-1])
print(f"{dP_unit_vectors_left_sign=}")
dp_unit_vectors_right_sign  = np.einsum('ij,ij->i',dP_unit_vectors, right_sign-P[:-1])
print(f"{dp_unit_vectors_right_sign=}")

# One line from P -> dP_unit_vectors
one_line_dP_unit_vectors = (P[1:] - P[:-1]) / np.linalg.norm(P[1:] - P[:-1], axis=1)[:, None]
# Right Orthogonal
n_unit_vector = np.column_stack((one_line_dP_unit_vectors[:,1], -one_line_dP_unit_vectors[:,0]))


# given a processing index
x = 0
given_pIdx_one_line_dp_unit_vectors = (P[x+1] - P[x])/np.linalg.norm(P[x+1] - P[x])
print(f'{given_pIdx_one_line_dp_unit_vectors=}')

# left/right
left_sign_left_right_given_pIdx_one_line = np.dot(np.array([given_pIdx_one_line_dp_unit_vectors[1],-given_pIdx_one_line_dp_unit_vectors[0]]),np.array(left_sign-P[x]))
print(f"{left_sign_left_right_given_pIdx_one_line=}")
print(f"{'RIGHT' if left_sign_left_right_given_pIdx_one_line>0 else 'LEFT'}")
right_sign_left_right_given_pIdx_one_line = np.dot(np.array([given_pIdx_one_line_dp_unit_vectors[1],-given_pIdx_one_line_dp_unit_vectors[0]]),np.array(right_sign-P[x]))
print(f"{'RIGHT' if right_sign_left_right_given_pIdx_one_line>0 else 'LEFT'}")

# Forward/Backwards
left_sign_front_back_given_pIdx_one_line = np.dot(((P[x+1] - P[x])/np.linalg.norm(P[x+1] - P[x])), left_sign-P[x])
print(f"{'FRONT' if left_sign_front_back_given_pIdx_one_line>0 else 'BACK'}")
right_sign_front_back_given_pIdx_one_line = np.dot(((P[x+1] - P[x])/np.linalg.norm(P[x+1] - P[x])), right_sign-P[x])
print(f"{'FRONT' if right_sign_front_back_given_pIdx_one_line>0 else 'BACK'}")
#
