from abc import ABC, abstractmethod
from typing import Tuple, List, Optional


class Chess_Piece(ABC):
    def __init__(
        self,
        ID: str,
        initial_position: Optional[Tuple[int, int]],
        color: str,
        direction: str,
        board_size: Tuple[int, int] = (8, 8)
    ):
        """
        Initialize a Chess_Piece object.

        :param ID: Unique identifier for the piece
        :param initial_position: Initial position on the board as a tuple (x, y)
        :param color: Color of the piece
        :param direction: Direction the piece is facing ("UP" or "DOWN")
        :param board_size: Size of the chess board as a tuple (width, height), default is (8, 8)
        """
        self._ID: str = ID
        self._color: str = color
        self._direction: str = direction
        self._board_size: Tuple[int, int] = board_size
        self._position: Optional[Tuple[int, int]] = None
        if initial_position:
            self.place(initial_position)

    @property
    def ID(self) -> str:
        """Return the unique identifier of the piece."""
        return self._ID

    def get_ID(self) -> str:
        """Return the unique identifier of the piece."""
        return self._ID

    @property
    def position(self) -> Optional[Tuple[int, int]]:
        """Return the current position of the piece on the board."""
        return self._position

    def get_position(self) -> Optional[Tuple[int, int]]:
        """Return the current position of the piece on the board."""
        return self._position if self._position is not None else (None, None)

    @property
    def color(self) -> str:
        """Return the color of the piece."""
        return self._color

    def get_color(self) -> str:
        """Return the color of the piece."""
        return self._color

    @property
    def direction(self) -> str:
        """Return the direction the piece is facing."""
        return self._direction

    def get_direction(self) -> str:
        """Return the direction the piece is facing."""
        return self._direction

    @property
    def board_size(self) -> Tuple[int, int]:
        """Return the size of the chess board."""
        return self._board_size

    def get_board_size(self) -> Tuple[int, int]:
        """Return the size of the chess board."""
        return self._board_size

    @staticmethod
    def _is_valid_position(position: Tuple[int, int], board_size: Tuple[int, int]) -> bool:
        """
        Check if a given position is valid on the board.

        :param position: Position to check as a tuple (x, y)
        :param board_size: Size of the chess board as a tuple (width, height)
        :return: True if the position is valid, False otherwise
        """
        x, y = position
        width, height = board_size
        return 0 <= x < width and 0 <= y < height

    def is_piece_on_board(self) -> bool:
        """Check if the piece is currently on the chess board."""
        return self._position is not None

    def place(self, position: Tuple[int, int]) -> None:
        """
        Place the piece on the board at the given position if it's not already on the board.

        :param position: Position to place the piece as a tuple (x, y)
        """
        if not self.is_piece_on_board() and self._is_valid_position(position, self._board_size):
            self._position = position

    def remove(self) -> None:
        """
        Remove the piece from the board.
        """
        self._position = None

    def move(self, new_position: Tuple[int, int]) -> None:
        """
        Move the piece to a new position on the board if it's a valid move.

        :param new_position: New position to move the piece to as a tuple (x, y)
        """
        if self.is_piece_on_board() and new_position in self.get_valid_moves():
            self._position = new_position

    def take(self, other_piece: 'Chess_Piece') -> None:
        """
        Take another piece on the board.

        :param other_piece: The Chess_Piece object to be taken
        """
        if not self.is_piece_on_board() or not other_piece.is_piece_on_board():
            return
        if other_piece.get_position() in self.get_valid_moves():
            self._position = other_piece.get_position()
            other_piece.remove()

    @abstractmethod
    def get_valid_moves(self) -> List[Tuple[int, int]]:
        """
        Get a list of valid moves for the piece.

        :return: A list of tuples representing valid positions the piece can move to
        """
        pass

    def __str__(self) -> str:
        """Return a string representation of the chess piece."""
        return (f"{self.__class__.__name__}("
                f"ID: {self._ID}, "
                f"Position: {self._position}, "
                f"Color: {self._color}, "
                f"Direction: {self._direction})")