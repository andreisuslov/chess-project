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

    def place(self, position: Tuple[int, int]) -> None:
        """
        Place the pawn on the board if it's not already on the board.

        :param position: Position to place the pawn as a tuple (x, y)
        """
        super().place(position)

    def get_valid_moves(self, board: Optional['Board'] = None) -> List[Tuple[int, int]]:
        """
        Get a list of valid moves for the Pawn.

        :param board: The Board object to check for collisions (optional)
        :return: A list of tuples representing valid positions the Pawn can move to
        """
        if not self.is_piece_on_board():
            return []

        valid_moves = []
        x, y = self.get_position()
        direction_modifier = 1 if self.get_direction() == "UP" else -1

        # Move one space forward
        new_y = y + direction_modifier
        if self._is_valid_position((x, new_y), self.get_board_size()):
            # Check collision if board is provided
            if board is None or board.get_piece_at((x, new_y)) is None:
                valid_moves.append((x, new_y))

                # Check if it's the Pawn's first move
                is_first_move_up = self.get_direction() == "UP" and y == 1
                is_first_move_down = self.get_direction() == "DOWN" and y == self.get_board_size()[1] - 2

                if is_first_move_up or is_first_move_down:
                    new_y_2 = y + 2 * direction_modifier
                    if self._is_valid_position((x, new_y_2), self.get_board_size()):
                        if board is None or board.get_piece_at((x, new_y_2)) is None:
                            valid_moves.append((x, new_y_2))
        
        # Captures
        if board:
            for dx in [-1, 1]:
                capture_x = x + dx
                capture_y = y + direction_modifier
                if self._is_valid_position((capture_x, capture_y), self.get_board_size()):
                    piece_at_target = board.get_piece_at((capture_x, capture_y))
                    if piece_at_target and piece_at_target.color != self.color:
                        valid_moves.append((capture_x, capture_y))

        return valid_moves

    def take(self, other_piece: 'Chess_Piece') -> None:
        """
        Take another piece on the board according to Pawn's special taking rules.

        :param other_piece: The Chess_Piece object to be taken
        """
        if not self.is_piece_on_board() or not other_piece.is_piece_on_board():
            return

        x, y = self.get_position()
        other_x, other_y = other_piece.get_position()
        direction_modifier = 1 if self.get_direction() == "UP" else -1

        valid_take_positions = [
            (x - 1, y + direction_modifier),
            (x + 1, y + direction_modifier)
        ]

        if (other_x, other_y) in valid_take_positions:
            self._position = other_piece.get_position()
            other_piece.remove()
        # Remove the else clause that was raising the ValueError

    def move(self, new_position: Tuple[int, int]) -> None:
        """
        Move the pawn to a new position on the board.

        :param new_position: New position to move the pawn to as a tuple (x, y)
        """
        if not self.is_piece_on_board():
            return
        if new_position in self.get_valid_moves():
            self._position = new_position

    def replace(self, new_piece: 'Chess_Piece') -> None:
        """
        Replace the Pawn with another chess piece.

        :param new_piece: The Chess_Piece object to replace this Pawn
        """
        if not self.is_piece_on_board() or new_piece.is_piece_on_board():
            return

        new_piece.place(self.get_position())
        self.remove()

    def __str__(self) -> str:
        """
        Return a string representation of the Pawn.

        :return: String representation of the Pawn
        """
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

    def get_valid_moves(self, board: Optional['Board'] = None) -> List[Tuple[int, int]]:
        """
        Get a list of valid moves for the Rook.

        :param board: The Board object to check for collisions (optional)
        :return: A list of tuples representing valid positions the Rook can move to
        """
        if not self.is_piece_on_board():
            return []

        valid_moves = []
        x, y = self.position
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in directions:
            for i in range(1, max(self.board_size)):
                new_x, new_y = x + dx * i, y + dy * i
                if not self._is_valid_position((new_x, new_y), self.board_size):
                    break
                
                if board:
                    piece_at_target = board.get_piece_at((new_x, new_y))
                    if piece_at_target:
                        if piece_at_target.color != self.color:
                            valid_moves.append((new_x, new_y))
                        break # Blocked by piece (friend or foe)
                
                valid_moves.append((new_x, new_y))

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

    def get_valid_moves(self, board: Optional['Board'] = None) -> List[Tuple[int, int]]:
        """
        Get a list of valid moves for the Queen.

        :param board: The Board object to check for collisions (optional)
        :return: A list of tuples representing valid positions the Queen can move to
        """
        if not self.is_piece_on_board():
            return []

        valid_moves = []
        x, y = self.position
        
        # Combine Rook (straight) and Bishop (diagonal) directions
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0), # Straight
            (1, 1), (1, -1), (-1, 1), (-1, -1) # Diagonal
        ]

        for dx, dy in directions:
            for i in range(1, max(self.board_size)):
                new_x, new_y = x + dx * i, y + dy * i
                if not self._is_valid_position((new_x, new_y), self.board_size):
                    break
                
                if board:
                    piece_at_target = board.get_piece_at((new_x, new_y))
                    if piece_at_target:
                        if piece_at_target.color != self.color:
                            valid_moves.append((new_x, new_y))
                        break # Blocked
                
                valid_moves.append((new_x, new_y))

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

    def get_valid_moves(self, board: Optional['Board'] = None) -> List[Tuple[int, int]]:
        """
        Get a list of valid moves for the Knight.

        :param board: The Board object to check for collisions (optional)
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

        valid_moves = []
        for move in potential_moves:
            if self._is_valid_position(move, self.board_size):
                if board:
                    piece_at_target = board.get_piece_at(move)
                    if piece_at_target and piece_at_target.color == self.color:
                        continue # Blocked by friendly piece
                valid_moves.append(move)

        return valid_moves

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

    def get_valid_moves(self, board: Optional['Board'] = None) -> List[Tuple[int, int]]:
        """
        Get a list of valid moves for the King.

        :param board: The Board object to check for collisions (optional)
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

        valid_moves = []
        for move in potential_moves:
            if self._is_valid_position(move, self.board_size):
                if board:
                    piece_at_target = board.get_piece_at(move)
                    if piece_at_target and piece_at_target.color == self.color:
                        continue # Blocked by friendly piece
                valid_moves.append(move)

        return valid_moves

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

    def get_valid_moves(self, board: Optional['Board'] = None) -> List[Tuple[int, int]]:
        """
        Get a list of valid moves for the Bishop.

        :param board: The Board object to check for collisions (optional)
        :return: A list of tuples representing valid positions the Bishop can move to
        """
        if not self.is_piece_on_board():
            return []

        valid_moves = []
        x, y = self.position
        
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            for i in range(1, max(self.board_size)):
                new_x, new_y = x + dx * i, y + dy * i
                if not self._is_valid_position((new_x, new_y), self.board_size):
                    break
                
                if board:
                    piece_at_target = board.get_piece_at((new_x, new_y))
                    if piece_at_target:
                        if piece_at_target.color != self.color:
                            valid_moves.append((new_x, new_y))
                        break # Blocked
                
                valid_moves.append((new_x, new_y))

        return valid_moves

    def __str__(self) -> str:
        """Return a string representation of the Bishop."""
        return f"Bishop({super().__str__()})"
