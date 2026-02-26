from datetime import datetime

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
                    self.placed_pieces.append(cell)

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
        shape_fits = True
        for row_num, row in enumerate(shape):
            for col_num, cell in enumerate(row):
                r, c = row_in + row_num, col_in + col_num
                if r < self.board_height and c < self.board_width:
                    if cell == 1 and self.board_mask[r][c] == 0:
                        self.board_mask[r][c] = shape_id_in
                    elif cell == 1:
                        shape_fits = False
                        break
                elif cell == 1:
                    shape_fits = False
                    break

        # If the shape doesn't fit we need to remove it
        if not shape_fits:
            self.remove_shape(shape_id_in)

        # Are we creating hole that are too small to be filled
        elif self.has_unfillable_holes(shape_id_in):
            self.remove_shape(shape_id_in)

        # Do we have enough holes to accomodate the remaining shapes
        elif not self.has_enought_holes(shape_id_in):
            self.remove_shape(shape_id_in)
        else:
            self.placed_pieces.append(shape_id_in)
        return shape_fits

    # This method will check the current state of the board to make sure
    # for any holes we create can possibly be filled by an exsisting piece that hasn't been placed
    def has_unfillable_holes(self, shape_id_in):
        visited = [[False for _ in row] for row in self.board_mask]
        hole_sizes = []

        def flood_fill(r, c):
            if r < 0 or c < 0 or r >= len(self.board_mask) or c >= len(self.board_mask[0]):
                return 0
            if visited[r][c] or self.board_mask[r][c] != 0:
                return 0
            visited[r][c] = True
            size = 1
            size += flood_fill(r + 1, c)
            size += flood_fill(r - 1, c)
            size += flood_fill(r, c + 1)
            size += flood_fill(r, c - 1)
            return size

        for r in range(len(self.board_mask)):
            for c in range(len(self.board_mask[0])):
                if not visited[r][c] and self.board_mask[r][c] == 0:
                    hole_size = flood_fill(r, c)
                    hole_sizes.append(hole_size)

        remaining_shapes = [self.shapes[s_id] for s_id in self.shapes if s_id not in self.placed_pieces]
        if shape_id_in in remaining_shapes:
            remaining_shapes.remove(shape_id_in)
        shape_sizes = [sum(cell for row in s.piece_shape for cell in row) for s in remaining_shapes]

        if not shape_sizes:
            return False  # no remaining pieces; all holes are now unfillable or filled

        min_piece_size = min(shape_sizes)
        for hole in hole_sizes:
            if hole < min_piece_size:
                return True  # at least one hole is too small to be filled by any remaining piece

        return False  # all holes are potentially fillable

    # This method will check the current state of the board to make sure
    # there is enough spaces for all the remaining pieces to possibly fill the board. (it doesn't check the shape)
    def has_enought_holes(self, shape_id_in):
        total_hole_count = 0
        for row in self.board_mask:
            for cell in row:
                if cell == 0:
                    total_hole_count += 1

        total_shape_blocks = 0
        for shape_id in self.shapes:
            if shape_id not in self.placed_pieces and shape_id != shape_id_in:
                for row in self.shapes[shape_id].original_piece_shape:
                    for cell in row:
                        if cell == 1:
                            total_shape_blocks+=1

        if total_hole_count != total_shape_blocks:
            return False  # Prune this path
        return True

    def place_shape_TL_to_BR(self, shape_id_in):
        for row_num, row in enumerate(self.board_mask):
            for col_num, _ in enumerate(row):
                if self.place_shape(shape_id_in, row_num, col_num):
                    return True
        return False

    def remove_shape(self, shape_id_in):
        for row_num, row in enumerate(self.board_mask):
            for col_num, cell in enumerate(row):
                if cell == shape_id_in:
                    self.board_mask[row_num][col_num] = 0
        self.placed_pieces = [x for x in self.placed_pieces if x != shape_id_in]

    def is_in_win_state(self):
        return all(cell != 0 for row in self.board_mask for cell in row)

    def are_arrays_equal(self, board1_in, board2_in):
        return board1_in == board2_in
