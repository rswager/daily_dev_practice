import copy


class Shapes:
    def __init__(self, id_number_in, piece_shape_in, color_in, flip_affected_in=True, rotate_once_in=False):
        self.id_number = id_number_in
        self.original_piece_shape = copy.deepcopy(piece_shape_in)
        self.piece_shape = copy.deepcopy(piece_shape_in)
        self.rotation = 0
        self.horizontal_flip = 0
        self.color = color_in
        self.flip_affected = flip_affected_in
        self.rotate_once = rotate_once_in
        self.piece_size = sum(sum(x) for x in self.original_piece_shape)

    def get_movements(self, forced_position=False):
        movements = {self.id_number: []}
        if forced_position:
            movements[self.id_number] = [(0, False)]
        else:
            if self.rotate_once:
                movements[self.id_number] += [(0, False),
                                              (90, False)]
            else:
                movements[self.id_number] += [(0, False),
                                              (90, False),
                                              (180, False),
                                              (270, False)]
                if self.flip_affected:
                    movements[self.id_number] += [(0, True),
                                                  (90, True),
                                                  (180, True),
                                                  (270, True)]
        return movements

    def hex_to_rgb(self, hex_color):
        """Convert hex color (e.g., '#FF5733') to an (R, G, B) tuple."""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

    def print_shape(self):
        """Draws a grid in the console using '█' for 1s and spaces for 0s, with custom hex color."""
        r, g, b = self.hex_to_rgb(self.color)

        for row in self.piece_shape:
            for cell in row:
                if cell == 1:
                    # ANSI 24-bit RGB foreground color code + '█'
                    print(f"\033[38;2;{r};{g};{b}m█\033[0m", end="")
                else:
                    print(" ", end="")  # space for 0s
            print()  # Newline for next row

    def rotate_90_clockwise(self):
        self.piece_shape = [list(row) for row in zip(*self.piece_shape[::-1])]
        self.rotation = (self.rotation + 90) % 360

    def flip_horizontal(self):
        self.piece_shape = [row[::-1] for row in self.piece_shape]
        self.horizontal_flip = (self.horizontal_flip + 1) % 2

    def set_shape(self, rotation_in, flip_in):
        self.piece_shape = copy.deepcopy(self.original_piece_shape)
        self.rotation = 0
        self.horizontal_flip = 0
        if flip_in and not self.horizontal_flip:
            self.flip_horizontal()

        while self.rotation != rotation_in:
            self.rotate_90_clockwise()
