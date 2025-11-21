from typing import Tuple, Optional
from board import Board
from pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "white"
        self.setup_board()

    def setup_board(self):
        # Setup White Pieces
        self.board.place_piece(Rook("WR1", (0, 0), "white", "UP"), (0, 0))
        self.board.place_piece(Knight("WN1", (1, 0), "white", "UP"), (1, 0))
        self.board.place_piece(Bishop("WB1", (2, 0), "white", "UP"), (2, 0))
        self.board.place_piece(Queen("WQ", (3, 0), "white", "UP"), (3, 0))
        self.board.place_piece(King("WK", (4, 0), "white", "UP"), (4, 0))
        self.board.place_piece(Bishop("WB2", (5, 0), "white", "UP"), (5, 0))
        self.board.place_piece(Knight("WN2", (6, 0), "white", "UP"), (6, 0))
        self.board.place_piece(Rook("WR2", (7, 0), "white", "UP"), (7, 0))
        for i in range(8):
            self.board.place_piece(Pawn(f"WP{i+1}", (i, 1), "white", "UP"), (i, 1))

        # Setup Black Pieces
        self.board.place_piece(Rook("BR1", (0, 7), "black", "DOWN"), (0, 7))
        self.board.place_piece(Knight("BN1", (1, 7), "black", "DOWN"), (1, 7))
        self.board.place_piece(Bishop("BB1", (2, 7), "black", "DOWN"), (2, 7))
        self.board.place_piece(Queen("BQ", (3, 7), "black", "DOWN"), (3, 7))
        self.board.place_piece(King("BK", (4, 7), "black", "DOWN"), (4, 7))
        self.board.place_piece(Bishop("BB2", (5, 7), "black", "DOWN"), (5, 7))
        self.board.place_piece(Knight("BN2", (6, 7), "black", "DOWN"), (6, 7))
        self.board.place_piece(Rook("BR2", (7, 7), "black", "DOWN"), (7, 7))
        for i in range(8):
            self.board.place_piece(Pawn(f"BP{i+1}", (i, 6), "black", "DOWN"), (i, 6))

    def play_turn(self, start_pos: Tuple[int, int], end_pos: Tuple[int, int]) -> bool:
        piece = self.board.get_piece_at(start_pos)
        
        if not piece:
            print("No piece at start position.")
            return False
        
        if piece.color != self.turn:
            print(f"It's {self.turn}'s turn. You cannot move {piece.color} pieces.")
            return False
        
        valid_moves = piece.get_valid_moves(self.board)
        if end_pos not in valid_moves:
            print(f"Invalid move for {piece.__class__.__name__} at {start_pos} to {end_pos}.")
            return False
        
        # Execute move
        self.board.move_piece(piece, end_pos)
        
        # Switch turn
        self.turn = "black" if self.turn == "white" else "white"
        return True

    def get_board_state(self):
        """
        Return the board state as a list of lists for the frontend.
        Each cell contains {'type': 'Pawn', 'color': 'white'} or None.
        """
        state = []
        for y in range(self.board.height - 1, -1, -1):
            row = []
            for x in range(self.board.width):
                piece = self.board.get_piece_at((x, y))
                if piece:
                    row.append({
                        'type': piece.__class__.__name__,
                        'color': piece.color,
                        'id': piece.ID
                    })
                else:
                    row.append(None)
            state.append(row)
        return state

    def start_cli(self):
        while True:
            print(self.board)
            print(f"{self.turn.capitalize()}'s turn")
            try:
                move_input = input("Enter move (x1,y1 x2,y2) or 'quit': ")
                if move_input.lower() == 'quit':
                    break
                
                start_str, end_str = move_input.split()
                x1, y1 = map(int, start_str.split(','))
                x2, y2 = map(int, end_str.split(','))
                
                if self.play_turn((x1, y1), (x2, y2)):
                    print("Move successful!")
                else:
                    print("Move failed, try again.")
            except ValueError:
                print("Invalid input format. Use 'x1,y1 x2,y2'.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    game = Game()
    game.start_cli()
