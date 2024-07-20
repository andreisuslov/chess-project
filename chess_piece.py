from abc import ABC, abstractmethod


class Chess_Piece(ABC):
    def __init__(self, ID, initial_position, color, direction, board_size=(8, 8)):
        self._ID = ID
        self._position = initial_position if self._is_valid_position(initial_position, board_size) else (None, None)
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

    @staticmethod
    def _is_valid_position(position, board_size):
        if position is None:
            return False
        x, y = position
        width, height = board_size
        return 0 <= x < width and 0 <= y < height

    def is_piece_on_board(self):
        has_position = self._position is not None
        is_not_default_position = self._position != (None, None)
        return has_position and is_not_default_position

    def place(self, position):
        position_is_valid = position is not None
        piece_not_on_board = not self.is_piece_on_board()
        within_board_limits = self._is_valid_position(position, self._board_size)

        if position_is_valid and piece_not_on_board and within_board_limits:
            self._position = position
        else:
            raise ValueError("Invalid placement: Position is not valid or piece is already on board.")

    def remove(self):
        if self.is_piece_on_board():
            self._position = (None, None)
        else:
            raise ValueError("Cannot remove: Piece is not on the board.")

    def move(self, new_position):
        new_position_is_valid = new_position is not None
        piece_is_on_board = self.is_piece_on_board()
        move_is_within_valid_moves = new_position in self.get_valid_moves()

        if new_position_is_valid and piece_is_on_board and move_is_within_valid_moves:
            self._position = new_position
        else:
            raise ValueError("Invalid move: New position is not valid or piece is not on board.")

    def take(self, other_piece):
        other_piece_is_valid = other_piece is not None
        piece_is_on_board = self.is_piece_on_board()
        other_piece_position_is_valid = other_piece.get_position() in self.get_valid_moves()

        if other_piece_is_valid and piece_is_on_board and other_piece_position_is_valid:
            self._position = other_piece.get_position()
            other_piece.remove()
        else:
            raise ValueError("Invalid take: Other piece is not valid or not in a valid position.")

    @abstractmethod
    def get_valid_moves(self):
        pass

    def __str__(self):
        return (f"{self.__class__.__name__}("
                f"ID: {self._ID}, "
                f"Position: {self._position}, "
                f"Color: {self._color}, "
                f"Direction: {self._direction})")
