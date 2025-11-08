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
        super().__init__(ID, initial_position, color, direction, board_size)

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        pass

    def take(self, other_piece: 'Chess_Piece') -> None:
        pass

    def replace(self, new_piece: 'Chess_Piece') -> None:
        pass

    def __str__(self) -> str:
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
        super().__init__(ID, initial_position, color, direction, board_size)

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        pass

    def __str__(self) -> str:
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
        super().__init__(ID, initial_position, color, direction, board_size)

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        pass

    def __str__(self) -> str:
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
        super().__init__(ID, initial_position, color, direction, board_size)

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        pass

    def __str__(self) -> str:
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
        super().__init__(ID, initial_position, color, direction, board_size)

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        pass

    def __str__(self) -> str:
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
        super().__init__(ID, initial_position, color, direction, board_size)

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        pass

    def __str__(self) -> str:
        pass
