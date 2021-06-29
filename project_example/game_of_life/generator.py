from game_of_life.cell import Cell


class Generator:
    """Game of life generator"""
    def __init__(self, size: int, seed_data: list = list()):
        """
        Constructor

        @param size: Board Size or matrix setting for x and y and must be minimum 2
        @param seed_data: List of tuples and teh tuple denoting x and y
        """
        if size < 2:
            raise AttributeError('"size" must must be no less than 2', size)
        self.size = size
        self.board = list()
        self._initialise_board()
        self._initialise_neighbours()
        self._seed(seed_data)

    def tick(self):
        """Regenerates all data in the cells generating the patterns from the seeded data"""
        for y in range(self.size):
            for x in range(self.size):
                cell = self.board[x][y]
                cell.re_generate()

    def _initialise_board(self):
        for y in range(self.size):
            col = list()
            for x in range(self.size):
                col.append(Cell())
            self.board.append(col)

    def _initialise_neighbours(self):
        def has_top_left_diagonal_cell():
            return above_y >= 0 and left_of_x > 0

        def has_top_middle_cell():
            return above_y >= 0

        def has_top_right_diagonal_cell():
            return above_y >= 0 and right_of_x < self.size

        def has_right_cell():
            return right_of_x < self.size

        def has_bottom_right_diagonal_cell():
            return below_y < self.size and right_of_x < self.size

        def has_bottom_middle_cell():
            return below_y < self.size

        def has_bottom_left_diagonal_cell():
            return below_y < self.size and left_of_x >= 0

        def has_left_cell():
            return left_of_x >= 0

        for y in range(self.size):
            for x in range(self.size):
                above_y = y - 1
                left_of_x = x - 1
                right_of_x = x + 1
                below_y = y + 1
                current_cell = self.board[x][y]
                # rotate around the current cell linearly
                if has_top_left_diagonal_cell():
                    neighbour = self.board[left_of_x][above_y]
                    current_cell.add_neighbour(neighbour)
                if has_top_middle_cell():
                    neighbour = self.board[x][above_y]
                    current_cell.add_neighbour(neighbour)
                if has_top_right_diagonal_cell():
                    neighbour = self.board[right_of_x][above_y]
                    current_cell.add_neighbour(neighbour)
                if has_right_cell():
                    neighbour = self.board[right_of_x][y]
                    current_cell.add_neighbour(neighbour)
                if has_bottom_right_diagonal_cell():
                    neighbour = self.board[right_of_x][below_y]
                    current_cell.add_neighbour(neighbour)
                if has_bottom_middle_cell():
                    neighbour = self.board[x][below_y]
                    current_cell.add_neighbour(neighbour)
                if has_bottom_left_diagonal_cell():
                    neighbour = self.board[left_of_x][below_y]
                    current_cell.add_neighbour(neighbour)
                if has_left_cell():
                    neighbour = self.board[left_of_x][y]
                    current_cell.add_neighbour(neighbour)

    def _seed(self, positions: list):
        for item in positions:
            x = item[0]
            y = item[1]
            cell = self.board[x][y]
            if cell is not None:
                cell.is_alive = True

    def __str__(self):
        return self._picture_board()

    def _picture_board(self):
        result = ' | '
        for y in range(self.size):
            if y != 0:
                result += '\n | '
            for x in range(self.size):
                item = str(self.board[x][y])
                result += f'{item} | '
        return result