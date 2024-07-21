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
        super().__init__(ID, color, board_size)
        self.position = initial_position
        self.direction = direction

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        """
        Get a list of valid moves for the Pawn.

        :return: A list of tuples representing valid positions the Pawn can move to
        """
        if not self.is_piece_on_board():
            return []

        valid_moves = []
        x, y = self.position
        direction_modifier = 1 if self.direction == "UP" else -1

        # Move one space forward
        new_y = y + direction_modifier
        if self._is_valid_position((x, new_y)):
            valid_moves.append((x, new_y))

        # Move two spaces forward if it's the Pawn's first move
        if (self.direction == "UP" and y == 1) or (self.direction == "DOWN" and y == self.board_size[1] - 2):
            new_y = y + 2 * direction_modifier
            if self._is_valid_position((x, new_y)):
                valid_moves.append((x, new_y))

        return valid_moves

    def take(self, other_piece: 'Chess_Piece') -> None:
        """
        Take another piece on the board.

        :param other_piece: The Chess_Piece object to be taken
        :raises ValueError: If the other piece is invalid or not in a valid position to be taken
        """
        if not self.is_piece_on_board() or not other_piece.is_piece_on_board():
            raise ValueError("Invalid take: One or both pieces are not on the board.")

        x, y = self.position
        other_x, other_y = other_piece.position
        direction_modifier = 1 if self.direction == "UP" else -1

        valid_take_positions = [
            (x - 1, y + direction_modifier),
            (x + 1, y + direction_modifier)
        ]

        if (other_x, other_y) in valid_take_positions:
            self.position = other_piece.position
            other_piece.remove()
        else:
            raise ValueError("Invalid take: The other piece is not in a valid position to be taken by a Pawn.")

    def replace(self, new_piece: 'Chess_Piece') -> None:
        """
        Replace the Pawn with another piece.

        :param new_piece: The Chess_Piece object to replace the Pawn
        :raises ValueError: If the new piece is already on the board or the Pawn is not on the board
        """
        if not self.is_piece_on_board():
            raise ValueError("Cannot replace: Pawn is not on the board.")
        if new_piece.is_piece_on_board():
            raise ValueError("Cannot replace: New piece is already on the board.")

        new_piece.place(self.position)
        self.remove()

    def __str__(self) -> str:
        """Return a string representation of the Pawn."""
        return f"Pawn({super().__str__()})"


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
        if not self.is_piece_on_board():
            return []

        valid_moves = []
        x, y = self.position

        # Horizontal moves
        for new_x in range(self.board_size[0]):
            if new_x != x:
                valid_moves.append((new_x, y))

        # Vertical moves
        for new_y in range(self.board_size[1]):
            if new_y != y:
                valid_moves.append((x, new_y))

        return valid_moves

    def __str__(self) -> str:
        """Return a string representation of the Rook."""
        return f"Rook({super().__str__()})"


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
        if not self.is_piece_on_board():
            return []

        # Start with the Rook's valid moves (horizontal and vertical)
        valid_moves = super().get_valid_moves()

        x, y = self.position

        # Add diagonal moves
        for i in range(1, max(self.board_size)):
            # Upper-right diagonal
            if self._is_valid_position((x + i, y + i), self.board_size):
                valid_moves.append((x + i, y + i))
            # Upper-left diagonal
            if self._is_valid_position((x - i, y + i), self.board_size):
                valid_moves.append((x - i, y + i))
            # Lower-right diagonal
            if self._is_valid_position((x + i, y - i), self.board_size):
                valid_moves.append((x + i, y - i))
            # Lower-left diagonal
            if self._is_valid_position((x - i, y - i), self.board_size):
                valid_moves.append((x - i, y - i))

        return valid_moves

    def __str__(self) -> str:
        """Return a string representation of the Queen."""
        return f"Queen({super().__str__()})"


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
        if not self.is_piece_on_board():
            return []

        x, y = self.position
        potential_moves = [
            (x + 2, y + 1), (x + 2, y - 1),
            (x - 2, y + 1), (x - 2, y - 1),
            (x + 1, y + 2), (x + 1, y - 2),
            (x - 1, y + 2), (x - 1, y - 2)
        ]

        return [move for move in potential_moves if self._is_valid_position(move, self.board_size)]

    def __str__(self) -> str:
        """Return a string representation of the Knight."""
        return f"Knight({super().__str__()})"


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
        if not self.is_piece_on_board():
            return []

        x, y = self.position
        potential_moves = [
            (x + 1, y), (x - 1, y),
            (x, y + 1), (x, y - 1),
            (x + 1, y + 1), (x + 1, y - 1),
            (x - 1, y + 1), (x - 1, y - 1)
        ]

        return [move for move in potential_moves if self._is_valid_position(move, self.board_size)]

    def __str__(self) -> str:
        """Return a string representation of the King."""
        return f"King({super().__str__()})"


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
        if not self.is_piece_on_board():
            return []

        valid_moves = []
        x, y = self.position

        for i in range(1, max(self.board_size)):
            # Upper-right diagonal
            if self._is_valid_position((x + i, y + i), self.board_size):
                valid_moves.append((x + i, y + i))
            # Upper-left diagonal
            if self._is_valid_position((x - i, y + i), self.board_size):
                valid_moves.append((x - i, y + i))
            # Lower-right diagonal
            if self._is_valid_position((x + i, y - i), self.board_size):
                valid_moves.append((x + i, y - i))
            # Lower-left diagonal
            if self._is_valid_position((x - i, y - i), self.board_size):
                valid_moves.append((x - i, y - i))

        return valid_moves

    def __str__(self) -> str:
        """Return a string representation of the Bishop."""
        return f"Bishop({super().__str__()})"
