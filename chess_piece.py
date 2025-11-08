from abc import ABC, abstractmethod


class Chess_Piece(ABC):
    def __init__(self, ID, initial_position, color, direction, board_size=(8, 8)):
        self._ID = ID
        self._position = initial_position if self._is_valid_position(initial_position) else (None, None)
        self._color = color
        self._direction = direction
        self._board_size = board_size

    def get_ID(self):
        return self._ID

    def get_position(self):
        return self._position

    def get_color(self):
        return self._color

    def get_direction(self):
        return self._direction

    def get_board_size(self):
        return self._board_size

    def _is_valid_position(self, position):
        x, y = position
        width, height = self._board_size
        return 0 <= x < width and 0 <= y < height

    def is_piece_on_board(self):
        return self._position != (None, None)

    def place(self, position):
        if not self.is_piece_on_board() and self._is_valid_position(position):
            self._position = position

    def remove(self):
        self._position = (None, None)

    def move(self, new_position):
        if self.is_piece_on_board() and new_position in self.get_valid_moves():
            self._position = new_position

    def take(self, other_piece):
        if self.is_piece_on_board() and other_piece.get_position() in self.get_valid_moves():
            self._position = other_piece.get_position()
            other_piece.remove()

    @abstractmethod
    def get_valid_moves(self):
        pass
