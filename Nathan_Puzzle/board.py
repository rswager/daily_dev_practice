from datetime import datetime

from shapes import Shapes


class Board:
    def __init__(self, shapes_in, weekday=False):
        self.date = ''
        self.shapes = shapes_in
        self.weekday = weekday
        if not self.weekday:
            self.board_height = 9
            self.board_width = 9
            self.board = [
                [' █ ', ' █ ', ' █ ', ' █ ', ' █ ', ' █ ', ' █ ', ' █ ', ' █ '],
                [' █ ', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', ' █ ', ' █ '],
                [' █ ', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', ' █ ', ' █ '],
                [' █ ', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' █ '],
                [' █ ', ' 8 ', ' 9 ', ' 10', ' 11', ' 12', ' 13', ' 14', ' █ '],
                [' █ ', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20', ' 21', ' █ '],
                [' █ ', ' 22', ' 23', ' 24', ' 25', ' 26', ' 27', ' 28', ' █ '],
                [' █ ', ' 29', ' 30', ' 31', ' █ ', ' █ ', ' █ ', ' █ ', ' █ '],
                [' █ ', ' █ ', ' █ ', ' █ ', ' █ ', ' █ ', ' █ ', ' █ ', ' █ ']
            ]
            self.board_mask = [
                [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                [-1,  0,  0,  0,  0,  0,  0, -1, -1],
                [-1,  0,  0,  0,  0,  0,  0, -1, -1],
                [-1,  0,  0,  0,  0,  0,  0,  0, -1],
                [-1,  0,  0,  0,  0,  0,  0,  0, -1],
                [-1,  0,  0,  0,  0,  0,  0,  0, -1],
                [-1,  0,  0,  0,  0,  0,  0,  0, -1],
                [-1,  0,  0,  0, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            ]
        else:
            self.board_height = 10
            self.board_width = 9
            self.board = [
                [' █ ', ' █ ', ' █ ', ' █ ', ' █ ', ' █ ', ' █ ', ' █ ', ' █ '],
                [' █ ', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', ' █ ', ' █ '],
                [' █ ', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', ' █ ', ' █ '],
                [' █ ', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' █ '],
                [' █ ', ' 8 ', ' 9 ', ' 10', ' 11', ' 12', ' 13', ' 14', ' █ '],
                [' █ ', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20', ' 21', ' █ '],
                [' █ ', ' 22', ' 23', ' 24', ' 25', ' 26', ' 27', ' 28', ' █ '],
                [' █ ', ' 29', ' 30', ' 31', 'Sun', 'Mon', 'Tue', 'Wed', ' █ '],
                [' █ ', ' █ ', ' █ ', ' █ ', ' █ ', 'Thr', 'Fri', 'Sat', ' █ '],
                [' █ ', ' █ ', ' █ ', ' █ ', ' █ ', ' █ ', ' █ ', ' █ ', ' █ ']
            ]
            self.board_mask = [
                [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                [-1,  0,  0,  0,  0,  0,  0, -1, -1],
                [-1,  0,  0,  0,  0,  0,  0, -1, -1],
                [-1,  0,  0,  0,  0,  0,  0,  0, -1],
                [-1,  0,  0,  0,  0,  0,  0,  0, -1],
                [-1,  0,  0,  0,  0,  0,  0,  0, -1],
                [-1,  0,  0,  0,  0,  0,  0,  0, -1],
                [-1,  0,  0,  0,  0,  0,  0,  0, -1],
                [-1, -1, -1, -1, -1,  0,  0,  0, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            ]
        self.placed_pieces = []

    def set_placed_pieces(self):
        self.placed_pieces = []  # Clear existing list before populating
        for row in self.board_mask:
            for cell in row:
                if cell > 0 and cell not in self.placed_pieces:
                    self.placed_pieces.append(cell) # add the shape_id if not already in list

    def print_visible_board(self):
        for row_num, row in enumerate(self.board_mask):
            for col_num, cell in enumerate(row):
                if cell <= 0:
                    print(self.board[row_num][col_num], end=' ')
                else:
                    r, g, b = self.shapes[cell].hex_to_rgb(self.shapes[cell].color)
                    print(f" \033[38;2;{r};{g};{b}m█\033[0m ", end=" ")
            print()  # Newline for next row
        print()

    def set_target_date(self, date_in):
        date_obj = datetime.strptime(date_in, "%Y-%m-%d")
        self.date = date_in
        month = date_obj.month
        day = date_obj.day
        self.board_mask[int((month - 1) / 6) + 1][((month - 1) % 6) + 1] = -2
        self.board_mask[int((day - 1) / 7) + 3][((day - 1) % 7) + 1] = -2
        if self.weekday:
            day_of_week = date_obj.weekday()
            # Monday
            if day_of_week == 0:
                self.board_mask[7][5] = -2
            # Tuesday
            elif day_of_week == 1:
                self.board_mask[7][6] = -2
            # Wednesday
            elif day_of_week == 2:
                self.board_mask[7][7] = -2
            # Thursday
            elif day_of_week == 3:
                self.board_mask[8][5] = -2
            # Friday
            elif day_of_week == 4:
                self.board_mask[8][6] = -2
            # Satruday
            elif day_of_week == 5:
                self.board_mask[8][7] = -2
            # Sunday
            else:
                self.board_mask[7][4] = -2

    def place_shape(self, shape_id_in, row_in, col_in):
        shape = self.shapes[shape_id_in].piece_shape
        for row_num, row in enumerate(shape):
            for col_num, cell in enumerate(row):
                r, c = row_in + row_num, col_in + col_num
                # Place on the board
                if cell == 1:
                    self.board_mask[r][c] = shape_id_in

    # Check if a shape could fit at a given location without actually placing it
    def shape_can_fit(self, shape_id_in, row_in, col_in):
        shape = self.shapes[shape_id_in].piece_shape
        for row_num, row in enumerate(shape):
            for col_num, cell in enumerate(row):
                r, c = row_in + row_num, col_in + col_num
                if cell == 1:
                    if r >= self.board_height or c >= self.board_width:
                        return False
                    if self.board_mask[r][c] != 0:
                        return False
        return True

    # This method will check the current state of the board to make sure
    # there is enough spaces for all the remaining pieces to possibly fill the board. (it doesn't check the shape)
    def has_enough_holes(self, shape_id_in):
        total_remaining_hole_count = 0
        for r in range(self.board_height):
            for c in range(self.board_width):
                total_remaining_hole_count += 1 if self.board_mask[r][c] == 0 else 0

        total_remaining_shape_holes_needed = 0
        for shape_id in self.shapes:
            if shape_id not in self.placed_pieces and shape_id != shape_id_in:
                total_remaining_shape_holes_needed += self.shapes[shape_id].piece_size

        # The remaining holes should account for the remaining shapes
        if total_remaining_hole_count != total_remaining_shape_holes_needed:
            return False  # Prune this path
        return True

    # This method will check the current state of the board to make sure
    # for any holes we create can possibly be filled by an existing piece that hasn't been placed
    def has_unfillable_holes(self, shape_id_in):
        remaining_hole_sizes = self.get_hole_sizes()

        # get the remaining shapes
        remaining_shapes_sizes = []
        for shape_id in self.shapes:
            if shape_id not in self.placed_pieces and shape_id != shape_id_in:
                remaining_shapes_sizes.append(self.shapes[shape_id].piece_size)

        if len(remaining_shapes_sizes) == 0:
            return False

        smallest_piece = min(remaining_shapes_sizes)

        # If any hole is smaller than the smallest remaining piece,
        # it can never be filled
        for hole in remaining_hole_sizes:
            if hole < smallest_piece:
                return True

        return False


    def get_hole_sizes(self):

        visited = [[False for _ in row] for row in self.board_mask]
        groups = []

        def dfs(r, c):
            # Check bounds
            if r < 0 or r >= self.board_height or c < 0 or c >= self.board_width:
                return 0

            # Stop if not zero or already visited
            if self.board_mask[r][c] != 0 or visited[r][c]:
                return 0

            visited[r][c] = True

            # Count this cell
            count = 1

            # Explore neighbors (4-directional)
            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)

            return count

        for r in range(self.board_height):
            for c in range(self.board_width):
                if self.board_mask[r][c] == 0 and not visited[r][c]:
                    group_size = dfs(r, c)
                    groups.append(group_size)

        return groups

    def can_fit_next_pieces(self, shape_id_in):
        # get the remaining_pieces
        remaining_shapes = []
        for shape_id in self.shapes:
            if shape_id not in self.placed_pieces and shape_id != shape_id_in:
                remaining_shapes.append(shape_id)

        for shape_id in remaining_shapes:
            shape = self.shapes[shape_id]
            shape_fit = False
            # need to go over all the orientations
            movements = shape.get_movements(forced_position=False)[shape_id]
            for degree, flip in movements:
                # Set the shape
                shape.set_shape(degree, flip)
                # start seeing if it can place
                for r in range(self.board_height):
                    for c in range(self.board_width):
                        # if we can fit we break out
                        if self.shape_can_fit(shape_id, r, c):
                            shape_fit = True
                            break
                    if shape_fit:
                        break
                if shape_fit:
                    break
            if not shape_fit:
                return False
        return True

    def place_shape_TL_to_BR(self, shape_id_in):
        for row_num, row in enumerate(self.board_mask):
            for col_num, _ in enumerate(row):
                if self.shape_can_fit(shape_id_in, row_num, col_num):
                    # The shape can fit! Let's place it and test the rest of the cases
                    self.place_shape(shape_id_in, row_num, col_num)

                    # # Do we have enough holes to accommodate the remaining shapes
                    # if not self.has_enough_holes(shape_id_in):
                    #     self.remove_shape(shape_id_in)

                    # Are we creating hole that are too small to be filled
                    if self.has_unfillable_holes(shape_id_in):
                        self.remove_shape(shape_id_in)
                    #
                    # elif not self.can_fit_next_pieces(shape_id_in):
                    #     self.remove_shape(shape_id_in)
                    # We passed all the test so we can place.
                    else:
                        self.placed_pieces.append(shape_id_in)
                        return True
        return False

    def remove_shape(self, shape_id_in):
        for row_num in range(self.board_height):
            for col_num in range(self.board_width):
                if self.board_mask[row_num][col_num] == shape_id_in:
                    self.board_mask[row_num][col_num] = 0
        if shape_id_in in self.placed_pieces:
            self.placed_pieces.remove(shape_id_in)

    def is_in_win_state(self):
        return all(cell != 0 for row in self.board_mask for cell in row)

    def are_arrays_equal(self, board1_in, board2_in):
        return board1_in == board2_in

if __name__ == '__main__':
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
    board = Board(weekday=False, shapes_in=shape_list)
    board.set_target_date(date_in='2025-03-07')
    board.place_shape_TL_to_BR(1)
    board.print_visible_board()
    board.place_shape_TL_to_BR(2)
    board.print_visible_board()
    board.place_shape_TL_to_BR(3)
    board.print_visible_board()
    board.place_shape_TL_to_BR(4)
    board.print_visible_board()
    board.place_shape_TL_to_BR(5)
    board.print_visible_board()
    board.place_shape_TL_to_BR(6)
    board.print_visible_board()
    board.place_shape_TL_to_BR(7)
    board.print_visible_board()
    board.place_shape_TL_to_BR(8)
    board.print_visible_board()