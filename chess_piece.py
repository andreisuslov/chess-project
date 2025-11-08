from abc import ABC, abstractmethod


class Chess_Piece(ABC):
    def __init__(self, ID, initial_position, color, direction, board_size=(8, 8)):
        """
        Initialize a Chess_Piece object.

        :param ID: Unique identifier for the piece
        :param initial_position: Initial position on the board as a tuple (x, y)
        :param color: Color of the piece
        :param direction: Direction the piece is facing ("UP" or "DOWN")
        :param board_size: Size of the chess board as a tuple (width, height), default is (8, 8)
        """
        self._ID = ID
        self._position = initial_position if self._is_valid_position(initial_position, board_size) else (None, None)
        self._color = color
        self._direction = direction
        self._board_size = board_size

    def get_ID(self):
        """Return the unique identifier of the piece."""
        return self._ID

    def get_position(self):
        """Return the current position of the piece on the board."""
        return self._position

    def get_color(self):
        """Return the color of the piece."""
        return self._color

    def get_direction(self):
        """Return the direction the piece is facing."""
        return self._direction

    def get_board_size(self):
        """Return the size of the chess board."""
        return self._board_size

    @staticmethod
    def _is_valid_position(position, board_size):
        """
        Check if a given position is valid on the board.

        :param position: Position to check as a tuple (x, y)
        :param board_size: Size of the chess board as a tuple (width, height)
        :return: True if the position is valid, False otherwise
        """
        if position is None:
            return False
        x, y = position
        width, height = board_size
        return 0 <= x < width and 0 <= y < height

    def is_piece_on_board(self):
        """Check if the piece is currently on the chess board."""
        has_position = self._position is not None
        is_not_default_position = self._position != (None, None)
        return has_position and is_not_default_position

    def place(self, position):
        """
        Place the piece on the board at the given position.

        :param position: Position to place the piece as a tuple (x, y)
        :raises ValueError: If the position is invalid or the piece is already on the board
        """
        position_is_valid = position is not None
        piece_not_on_board = not self.is_piece_on_board()
        within_board_limits = self._is_valid_position(position, self._board_size)

        if position_is_valid and piece_not_on_board and within_board_limits:
            self._position = position
        else:
            raise ValueError("Invalid placement: Position is not valid or piece is already on board.")

    def remove(self):
        """
        Remove the piece from the board.

        :raises ValueError: If the piece is not on the board
        """
        if self.is_piece_on_board():
            self._position = (None, None)
        else:
            raise ValueError("Cannot remove: Piece is not on the board.")

    def move(self, new_position):
        """
        Move the piece to a new position on the board.

        :param new_position: New position to move the piece to as a tuple (x, y)
        :raises ValueError: If the new position is invalid or the piece is not on the board
        """
        new_position_is_valid = new_position is not None
        piece_is_on_board = self.is_piece_on_board()
        move_is_within_valid_moves = new_position in self.get_valid_moves()

        if new_position_is_valid and piece_is_on_board and move_is_within_valid_moves:
            self._position = new_position
        else:
            raise ValueError("Invalid move: New position is not valid or piece is not on board.")

    def take(self, other_piece):
        """
        Take another piece on the board.

        :param other_piece: The Chess_Piece object to be taken
        :raises ValueError: If the other piece is invalid or not in a valid position to be taken
        """
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
        """
        Get a list of valid moves for the piece.

        :return: A list of tuples representing valid positions the piece can move to
        """
        pass

    def __str__(self):
        """Return a string representation of the chess piece."""
        return (f"{self.__class__.__name__}("
                f"ID: {self._ID}, "
                f"Position: {self._position}, "
                f"Color: {self._color}, "
                f"Direction: {self._direction})")
