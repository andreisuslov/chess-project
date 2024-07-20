from chess_piece import Chess_Piece
from typing import Tuple, List, Optional


class Pawn(Chess_Piece):
    def __init__(
            self,
            ID: str,
            initial_position: Optional[Tuple[int, int]],
            color: str,
            direction: str,
            board_size: Tuple[int, int] = (8, 8)
    ):
        """
        Initialize a Pawn object.

        :param ID: Unique identifier for the piece
        :param initial_position: Initial position on the board as a tuple (x, y)
        :param color: Color of the piece
        :param direction: Direction the piece is facing ("UP" or "DOWN")
        :param board_size: Size of the chess board as a tuple (width, height), default is (8, 8)
        """
        super().__init__(ID, initial_position, color, direction, board_size)

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        """
        Get a list of valid moves for the Pawn.

        :return: A list of tuples representing valid positions the Pawn can move to
        """
        pass

    def take(self, other_piece: 'Chess_Piece') -> None:
        """
        Take another piece on the board.

        :param other_piece: The Chess_Piece object to be taken
        :raises ValueError: If the other piece is invalid or not in a valid position to be taken
        """
        pass

    def replace(self, new_piece: 'Chess_Piece') -> None:
        """
        Replace the Pawn with another piece.

        :param new_piece: The Chess_Piece object to replace the Pawn
        :raises ValueError: If the new piece is already on the board or the Pawn is not on the board
        """
        pass

    def __str__(self) -> str:
        """Return a string representation of the Pawn."""
        pass


class Rook(Chess_Piece):
    def __init__(
            self,
            ID: str,
            initial_position: Optional[Tuple[int, int]],
            color: str,
            direction: str,
            board_size: Tuple[int, int] = (8, 8)
    ):
        """
        Initialize a Rook object.

        :param ID: Unique identifier for the piece
        :param initial_position: Initial position on the board as a tuple (x, y)
        :param color: Color of the piece
        :param direction: Direction the piece is facing ("UP" or "DOWN")
        :param board_size: Size of the chess board as a tuple (width, height), default is (8, 8)
        """
        super().__init__(ID, initial_position, color, direction, board_size)

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        """
        Get a list of valid moves for the Rook.

        :return: A list of tuples representing valid positions the Rook can move to
        """
        pass

    def __str__(self) -> str:
        """Return a string representation of the Rook."""
        pass


class Queen(Rook):
    def __init__(
        self,
        ID: str,
        initial_position: Optional[Tuple[int, int]],
        color: str,
        direction: str,
        board_size: Tuple[int, int] = (8, 8)
    ):
        """
        Initialize a Queen object.

        :param ID: Unique identifier for the piece
        :param initial_position: Initial position on the board as a tuple (x, y)
        :param color: Color of the piece
        :param direction: Direction the piece is facing ("UP" or "DOWN")
        :param board_size: Size of the chess board as a tuple (width, height), default is (8, 8)
        """
        super().__init__(ID, initial_position, color, direction, board_size)

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        """
        Get a list of valid moves for the Queen.

        :return: A list of tuples representing valid positions the Queen can move to
        """
        pass

    def __str__(self) -> str:
        """Return a string representation of the Queen."""
        pass


class Knight(Chess_Piece):
    def __init__(
        self,
        ID: str,
        initial_position: Optional[Tuple[int, int]],
        color: str,
        direction: str,
        board_size: Tuple[int, int] = (8, 8)
    ):
        """
        Initialize a Knight object.

        :param ID: Unique identifier for the piece
        :param initial_position: Initial position on the board as a tuple (x, y)
        :param color: Color of the piece
        :param direction: Direction the piece is facing ("UP" or "DOWN")
        :param board_size: Size of the chess board as a tuple (width, height), default is (8, 8)
        """
        super().__init__(ID, initial_position, color, direction, board_size)

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        """
        Get a list of valid moves for the Knight.

        :return: A list of tuples representing valid positions the Knight can move to
        """
        pass

    def __str__(self) -> str:
        """Return a string representation of the Knight."""
        pass


class King(Chess_Piece):
    def __init__(
        self,
        ID: str,
        initial_position: Optional[Tuple[int, int]],
        color: str,
        direction: str,
        board_size: Tuple[int, int] = (8, 8)
    ):
        """
        Initialize a King object.

        :param ID: Unique identifier for the piece
        :param initial_position: Initial position on the board as a tuple (x, y)
        :param color: Color of the piece
        :param direction: Direction the piece is facing ("UP" or "DOWN")
        :param board_size: Size of the chess board as a tuple (width, height), default is (8, 8)
        """
        super().__init__(ID, initial_position, color, direction, board_size)

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        """
        Get a list of valid moves for the King.

        :return: A list of tuples representing valid positions the King can move to
        """
        pass

    def __str__(self) -> str:
        """Return a string representation of the King."""
        pass


class Bishop(Chess_Piece):
    def __init__(
        self,
        ID: str,
        initial_position: Optional[Tuple[int, int]],
        color: str,
        direction: str,
        board_size: Tuple[int, int] = (8, 8)
    ):
        """
        Initialize a Bishop object.

        :param ID: Unique identifier for the piece
        :param initial_position: Initial position on the board as a tuple (x, y)
        :param color: Color of the piece
        :param direction: Direction the piece is facing ("UP" or "DOWN")
        :param board_size: Size of the chess board as a tuple (width, height), default is (8, 8)
        """
        super().__init__(ID, initial_position, color, direction, board_size)

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        """
        Get a list of valid moves for the Bishop.

        :return: A list of tuples representing valid positions the Bishop can move to
        """
        pass

    def __str__(self) -> str:
        """Return a string representation of the Bishop."""
        pass
