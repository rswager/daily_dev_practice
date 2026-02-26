from shapes import *
from board import *
from collections import deque
import copy
import time


def board_to_tuple(board):
    return tuple(tuple(row) for row in board)

def format_seconds(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

start_time = time.time()
weekday = False
date = '2025-03-07'
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
force_shape_start_position = True
print("Date Entered: " + date)

initial_board = Board(shapes_in=shape_list, weekday=weekday)
initial_board.set_target_date(date)
initial_board.print_visible_board()


total_movements = {}
for shape_id in shape_list:
    total_movements.update(shape_list[shape_id].get_movements(forced_position=force_shape_start_position))

# BFS Initialization
OPEN = deque()
CLOSED = set()
OPEN.append(copy.deepcopy(initial_board.board_mask))
SOLVED = False
print("Processing...")
iterations = 0
while not SOLVED and len(OPEN) > 0:
    board_state = OPEN.popleft()
    # Create a new board for this state
    current_board = Board(shapes_in=shape_list, weekday=weekday)
    current_board.board_mask = copy.deepcopy(board_state)
    current_board.set_placed_pieces()
    if iterations % 1_000 == 0:
        print("Iteration-", iterations, "  Piece(s) Placed: " + str(len(current_board.placed_pieces)))
        current_board.print_visible_board()
    iterations +=1
    # Serialize and mark as visited
    serialized_state = board_to_tuple(current_board.board_mask)
    CLOSED.add(serialized_state)

    # check to see if we have reached a win state
    # If Yes we are DONE
    if current_board.is_in_win_state():
        print("SUCCESS")
        current_board.print_visible_board()
        SOLVED = True
        break
    # Try placing each unused shape with each transformation (Populated all the child nodes)
    for shape_id in total_movements:
        # We cannot place a piece more than once
        if shape_id not in current_board.placed_pieces:
            # Get all the orientations of the piece
            for degree, flip in total_movements[shape_id]:
                # Set the shape orientation
                shape_list[shape_id].set_shape(rotation_in=degree, flip_in=flip)
                temp_board = copy.deepcopy(current_board)
                # Attmept to place the piece
                if temp_board.place_shape_TL_to_BR(shape_id):
                    next_state = board_to_tuple(temp_board.board_mask)
                    # if we have successfully placed the piece we need
                    # to see if we have already made this move
                    if next_state not in CLOSED:
                        # If we have not we need to add it to the process list
                        OPEN.append(copy.deepcopy(temp_board.board_mask))

print(format_seconds(time.time()-start_time))
print("Processed Boards:", len(CLOSED))
