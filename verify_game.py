from game import Game

def verify_game():
    game = Game()
    print("Initial Board:")
    print(game.board)

    # Test 1: White Pawn Move
    print("\nTest 1: White Pawn Move (4,1) -> (4,3)")
    success = game.play_turn((4, 1), (4, 3))
    print(f"Move successful: {success}")
    print(game.board)
    assert success, "White pawn double move failed"

    # Test 2: Black Pawn Move
    print("\nTest 2: Black Pawn Move (3,6) -> (3,4)")
    success = game.play_turn((3, 6), (3, 4))
    print(f"Move successful: {success}")
    print(game.board)
    assert success, "Black pawn double move failed"

    # Test 3: White Knight Move
    print("\nTest 3: White Knight Move (1,0) -> (2,2)")
    success = game.play_turn((1, 0), (2, 2))
    print(f"Move successful: {success}")
    print(game.board)
    assert success, "White knight move failed"

    # Test 4: Invalid Move (Black's turn, trying to move White)
    print("\nTest 4: Invalid Move (White moving on Black's turn)")
    # Current turn should be White (after W, B, W moves? No: W(1), B(2), W(3). Now it's Black's turn)
    # Wait:
    # 1. W Pawn (4,1)->(4,3) -> Turn Black
    # 2. B Pawn (3,6)->(3,4) -> Turn White
    # 3. W Knight (1,0)->(2,2) -> Turn Black
    # So now it is Black's turn. Trying to move White piece should fail.
    success = game.play_turn((0, 0), (0, 1)) # White Rook
    print(f"Move successful: {success}")
    assert not success, "White moved on Black's turn!"

    # Test 5: Capture
    # Let's set up a capture.
    # Black moves Queen to diagonal (3,7) -> (0,4) ? No, blocked by pawns.
    # Let's move Black Pawn (4,6) -> (4,4)
    print("\nTest 5: Black Pawn Move (4,6) -> (4,4)")
    success = game.play_turn((4, 6), (4, 4))
    assert success

    # Now White Pawn at (4,3) takes Black Pawn at (3,4)? No, pawns capture diagonally.
    # White Pawn at (4,3). Black Pawn at (3,4).
    # White Pawn captures (3,4)? No, (4,3) captures (3,4) is (x-1, y+1).
    # White is UP. (4,3) -> (3,4) is (x-1, y+1). Correct.
    print("\nTest 6: White Pawn Capture (4,3) -> (3,4)")
    success = game.play_turn((4, 3), (3, 4))
    print(f"Move successful: {success}")
    print(game.board)
    assert success, "Capture failed"
    
    piece = game.board.get_piece_at((3, 4))
    assert piece.color == "white", "Capture did not replace piece correctly"

    print("\nAll tests passed!")

if __name__ == "__main__":
    verify_game()
