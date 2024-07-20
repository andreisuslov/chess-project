from abc import ABC, abstractmethod


class Chess_Piece(ABC):
    def __init__(self, ID, initial_position, color, direction, board_size=(8, 8)):
        self._ID = ID
        self._position = initial_position if self._is_valid_position(initial_position) else (None, None)
        self._color = color
        self._direction = direction
        self._board_size = board_size

    def _is_valid_position(self, position):
        x, y = position
        width, height = self._board_size
        return 0 <= x < width and 0 <= y < height

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
