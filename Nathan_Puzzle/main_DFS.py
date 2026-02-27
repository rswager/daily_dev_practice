import time

from shapes import *
from board import *
import copy

def board_to_tuple(board):
    return tuple(tuple(row) for row in board)

def format_seconds(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

def solve_dfs(board, total_movements, iteration_counter, depth=0):
    iteration_counter ["count"] += 1

    # 🔹 Print occasionally
    if iteration_counter["count"] % 100 == 0:
        print(
            f"Iterations: {iteration_counter['count']} | "
            f"Depth: {depth} | "
            f"Placed: {len(board.placed_pieces)}"
        )
        board.print_visible_board()

    # 1️⃣ Win check
    if board.is_in_win_state():
        return True

    # 2️⃣ Try each unused shape
    for shape_id in total_movements:

        if shape_id not in board.placed_pieces:

            for degree, flip in total_movements[shape_id]:

                # Set orientation
                board.shapes[shape_id].set_shape(
                    rotation_in=degree,
                    flip_in=flip
                )

                # Try placing (this already prunes)
                if board.place_shape_TL_to_BR(shape_id):

                    # Recurse deeper
                    if solve_dfs(board, total_movements, iteration_counter, depth + 1):
                        return True

                    # 🔄 Backtrack
                    board.remove_shape(shape_id)

            # Optional pruning:
            # If we picked a shape and none of its orientations worked,
            # don't try a different shape at this same depth.
            return False

    return False

start_time = time.time()
weekday = False
date = '2026-02-27'
if not weekday:
    shape_list = {
        1: Shapes(1, [[1, 1, 1], [1, 1, 1]], 'FF0000', flip_affected_in=False, rotate_once_in=True),
        2: Shapes(2, [[1, 1], [1, 0], [1, 0], [1, 0]], '0000FF'),
        3: Shapes(3, [[1, 1, 0, 0], [0, 1, 1, 1]], '00FF00'),
        4: Shapes(4, [[1, 0], [1, 1], [1, 0], [1, 0]], 'FFFF00'),
        5: Shapes(5, [[0, 0, 1], [1, 1, 1], [1, 0, 0]], '00FFFF'),
        6: Shapes(6, [[1, 0, 0], [1, 0, 0], [1, 1, 1]], '800080', flip_affected_in=False),
        7: Shapes(7, [[1, 0, 1], [1, 1, 1]], 'A52A2A', flip_affected_in=False),
        8: Shapes(8, [[0, 1], [1, 1], [1, 1]], 'FFA500')
    }
else:
    shape_list = {
        1: Shapes(1, [[1, 1, 1, 1], [1, 0, 0, 0]], 'FF0000'),
        2: Shapes(2, [[1, 1, 1, 1]], '0000FF', flip_affected_in=False, rotate_once_in=True),
        3: Shapes(3, [[1, 1, 1, 0], [0, 0, 1, 1]], '00FF00'),
        4: Shapes(4, [[0, 1, 0], [0, 1, 0], [1, 1, 1]], 'FFFF00', flip_affected_in=False),
        5: Shapes(5, [[1, 1], [1, 0], [1, 0]], '00FFFF'),
        6: Shapes(6, [[0, 1, 1], [0, 1, 0], [1, 1, 0]], '800080'),
        7: Shapes(7, [[0, 1], [1, 1], [1, 0]], 'A52A2A'),
        8: Shapes(8, [[1, 1, 1], [1, 0, 0], [1, 0, 0]], 'FFA500', flip_affected_in=False),
        9: Shapes(9, [[1, 1], [1, 1], [1, 0]], '228B22'),
        10: Shapes(10, [[1, 0, 1], [1, 1, 1]], 'FFC0CB', flip_affected_in=False)
    }

# BFS grows exponentially, so we can limit by orientating the piece(s) in one way
# The pieces are orientated in the March 7th Position
# Making this false will return a result eventually, but will take exponentially longer
#     Later testing results in about 1 hr to run with forced being False
force_shape_start_position = False
print("Date Entered: " + date)

initial_board = Board(shapes_in=shape_list, weekday=weekday)
initial_board.set_target_date(date)
initial_board.print_visible_board()

total_movements = {}
for shape_id in shape_list:
    total_movements.update(shape_list[shape_id].get_movements(forced_position=force_shape_start_position))

# Precompute movements
total_movements = {}
for shape_id, shape in shape_list.items():
    total_movements[shape_id] = shape.get_movements(
        forced_position=force_shape_start_position
    )[shape_id]

print("Solving with DFS...")
start_time = time.time()
iteration_counter = {"count": 0}
if solve_dfs(initial_board, total_movements, iteration_counter):
    print("SUCCESS")
    initial_board.print_visible_board()
else:
    print("No solution found.")

print("Time:", format_seconds(time.time() - start_time))


