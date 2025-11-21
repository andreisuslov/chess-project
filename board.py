from typing import Tuple, Optional, List
from chess_piece import Chess_Piece

class Board:
    def __init__(self, width: int = 8, height: int = 8):
        self.width = width
        self.height = height
        # Grid is a list of lists, where grid[y][x] holds the piece or None
        self.grid: List[List[Optional['Chess_Piece']]] = [[None for _ in range(width)] for _ in range(height)]

    def is_valid_position(self, position: Tuple[int, int]) -> bool:
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def get_piece_at(self, position: Tuple[int, int]) -> Optional['Chess_Piece']:
        if not self.is_valid_position(position):
            return None
        x, y = position
        return self.grid[y][x]

    def place_piece(self, piece: 'Chess_Piece', position: Tuple[int, int]):
        if not self.is_valid_position(position):
            raise ValueError(f"Invalid position: {position}")
        
        # If piece is already on board, remove it from old position
        if piece.position:
            old_x, old_y = piece.position
            self.grid[old_y][old_x] = None

        x, y = position
        # If there's a piece at the new position, it's being captured (logic handled by Game/Piece, but Board just overwrites)
        self.grid[y][x] = piece
        piece.place(position) # Update piece's internal state

    def remove_piece(self, piece: 'Chess_Piece'):
        if piece.position:
            x, y = piece.position
            if self.grid[y][x] == piece:
                self.grid[y][x] = None
            piece.remove()

    def move_piece(self, piece: 'Chess_Piece', new_position: Tuple[int, int]):
        if not self.is_valid_position(new_position):
            raise ValueError(f"Invalid position: {new_position}")
        
        self.place_piece(piece, new_position)

    def __str__(self):
        board_str = ""
        for y in range(self.height - 1, -1, -1):
            row_str = f"{y} "
            for x in range(self.width):
                piece = self.grid[y][x]
                if piece:
                    # Simple representation: First letter of class name + color (W/B)
                    # e.g., PW (Pawn White), KB (King Black)
                    symbol = piece.__class__.__name__[0]
                    if piece.__class__.__name__ == "Knight": # K is King, N is Knight usually, but let's stick to simple for now or fix
                        symbol = "N"
                    color = piece.color[0].upper()
                    row_str += f"[{symbol}{color}]"
                else:
                    row_str += "[  ]"
            board_str += row_str + "\n"
        board_str += "   " + " ".join([f" {x}  " for x in range(self.width)])
        return board_str
