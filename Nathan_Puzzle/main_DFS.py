from shapes import *
from board import *
import copy

def board_to_tuple(board):
    return tuple(tuple(row) for row in board)

shape_list = {
    1: Shapes(1, [[1, 1, 1], [1, 1, 1]], 'FF0000', False, True),
    2: Shapes(2, [[1, 1], [1, 0], [1, 0], [1, 0]], '0000FF'),
    3: Shapes(3, [[1, 1, 0, 0], [0, 1, 1, 1]], '00FF00'),
    4: Shapes(4, [[1, 0], [1, 1], [1, 0], [1, 0]], 'FFFF00'),
    5: Shapes(5, [[0, 0, 1], [1, 1, 1], [1, 0, 0]], '00FFFF'),
    6: Shapes(6, [[1, 0, 0], [1, 0, 0], [1, 1, 1]], '800080', False),
    7: Shapes(7, [[1, 0, 1], [1, 1, 1]], 'A52A2A', False),
    8: Shapes(8, [[0, 1], [1, 1], [1, 1]], 'FFA500')
}

date = '2025-03-07'

# The pieces are orientated in the March 7th Position
# Making this false will return a result eventually, but will take a little longer
# Most likely will exit with the max depth limit
force_shape_start_position = True
print("Date Entered: " + date)

initial_board = Board(shapes_in=shape_list)
initial_board.set_target_date(date)
initial_board.print_visible_board()

total_movements = {}
for shape_id in shape_list:
    total_movements.update(shape_list[shape_id].get_movements(forced_position=force_shape_start_position))

MAX_DEPTH_LIMIT = 100  # You can increase this if needed
SOLVED = False
iteration = 0

for depth_limit in range(1, MAX_DEPTH_LIMIT + 1):
    print(f"Trying depth limit: {depth_limit}")
    OPEN = [(copy.deepcopy(initial_board), 0)]
    CLOSED = set()

    while OPEN and not SOLVED:
        current_board, depth = OPEN.pop()
        board_signature = board_to_tuple(current_board.board_mask)

        if board_signature in CLOSED:
            continue
        CLOSED.add(board_signature)
        iteration += 1

        if current_board.is_in_win_state():
            print(f"SUCCESS at iteration: {iteration}, depth: {depth}")
            current_board.print_visible_board()
            SOLVED = True
            break

        if depth >= depth_limit:
            continue  # Skip expansion beyond current depth

        for shape_id in total_movements:
            if shape_id not in current_board.placed_pieces:
                for degree, flip in total_movements[shape_id]:
                    shape_list[shape_id].set_shape(rotation_in=degree, flip_in=flip)
                    temp_board = copy.deepcopy(current_board)
                    if temp_board.place_shape_TL_to_BR(shape_id):
                        OPEN.append((temp_board, depth + 1))

    if SOLVED:
        break

if not SOLVED:
    print(f"No solution found within depth limit {MAX_DEPTH_LIMIT}")
else:
    print(f"Total states explored: {iteration}")
