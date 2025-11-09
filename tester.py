"""
 Tester code for Lab 01.
"""

from chess_piece import Chess_Piece
from pieces import Pawn
from pieces import King
from pieces import Knight
from pieces import Bishop
from pieces import Rook
from pieces import Queen

pause = True

# I) Try to construct the Chess_Piece which should fail
print("I) Try to construct the Chess_Piece which should fail")
try:
    cp1 = Chess_Piece("GeneralPiece1", (0, 0), "red", "UP", (8, 8))
    print("Chess_Piece is not abstract.")
except TypeError:
    print("GOOD NEWS! Chess_Piece is abstract!")
except:
    print("Chess_Piece is not abstract.")
finally:
    print("-------------------------------------------------------------------------------")

# II) Test the inherited constructor in Pawn and its optional parameters
print("\nII) Test the inherited constructor in Pawn and its optional parameters")
try:
    pawn1 = Pawn("pawn1", (2, 1), "white", "UP", (10, 10))
    print("Pawn constructor appears to work correctly")
except:
    print("WARNING! Exception during Pawn construction!")

try:
    pawn2 = Pawn("pawn2", (3, 6), "black", "DOWN")
    print("Optional parameter in Pawn constructor appears to work correctly")
except:
    pawn2 = Pawn("pawn2", (3, 6), "black", "DOWN", (8, 8))
    print("WARNING! Optional parameter for Pawn failed! Falling back to full constructor.")

if isinstance(pawn1, Chess_Piece):
    print("Pawns are properly inheriting from Chess_Piece")
else:
    print("WARNING! Pawns are not inheriting from Chess_Piece")

# III) Test the accessor methods of Chess_Piece in Pawn
print("\nIII) Test the inherited accessor methods of Chess_Piece in Pawn")
print("pawn1\t\t= " + str(pawn1.get_ID()))
print("(2, 1)\t\t= " + str(pawn1.get_position()))
print("white\t\t= " + str(pawn1.get_color()))
print("UP\t\t= " + str(pawn1.get_direction()))
print("(10, 10)\t= " + str(pawn1.get_board_size()))
print("True\t\t= " + str(pawn1.is_piece_on_board()))
print("Valid moves?\t= " +
      ("WORKS!" if set(pawn1.get_valid_moves()) == set([(2, 2), (2, 3)]) else "Failed") +
      "\n\t\t" + str(pawn1.get_valid_moves()))
print()
print("pawn2\t\t= " + str(pawn2.get_ID()))
print("(3, 6)\t\t= " + str(pawn2.get_position()))
print("black\t\t= " + str(pawn2.get_color()))
print("DOWN\t\t= " + str(pawn2.get_direction()))
print("(8, 8)\t\t= " + str(pawn2.get_board_size()))
print("True\t\t= " + str(pawn2.is_piece_on_board()))
print("Valid moves?\t= " +
      ("WORKS!" if set(pawn2.get_valid_moves()) == set([(3, 5), (3, 4)]) else "Failed") +
      "\n\t\t" + str(pawn2.get_valid_moves()))

# IV) Test the inherited mutator methods of place and remove in Pawn
print("\nIV) Test the inherited mutator methods of place and remove in Pawn")
pawn1.place((0, 0))
print("(2, 1)\t\t= " + str(pawn1.get_position()))
pawn1.remove()
print("(None, None)\t= " + str(pawn1.get_position()))
pawn1.place((0, -1))
print("(None, None)\t= " + str(pawn1.get_position()))
pawn1.place((12, 5))
print("(None, None)\t= " + str(pawn1.get_position()))
pawn1.place((4, 1))
print("(4, 1)\t\t= " + str(pawn1.get_position()))

if pause:
    input()

# V) Test the inherited mutator methods of move and take in Pawn
print("\nV) Test the inherited mutator methods of move and take in Pawn")
pawn3 = Pawn("pawn1", (4, 2), "black", "DOWN", (10, 10))
pawn1.take(pawn3)
print("--------------------------------")
print("Make sure pawn3 is not taken by pawn1")
print("True\t\t= " + str(pawn3.is_piece_on_board()))
print("(4, 1)\t\t= " + str(pawn1.get_position()))
print("--------------------------------")
pawn1.move((4, 3))
print("(4, 3)\t\t= " + str(pawn1.get_position()))
pawn2.move((0, 0))
print("(3, 6)\t\t= " + str(pawn2.get_position()))
pawn2.move((3, 4))
print("(3, 4)\t\t= " + str(pawn2.get_position()))
pawn1.take(pawn2)
print("True\t\t= " + str(pawn1.is_piece_on_board()))
print("False\t\t= " + str(pawn2.is_piece_on_board()))
print("(3, 4)\t\t= " + str(pawn1.get_position()))
pawn1.move((4, 3))
print("(3, 4)\t\t= " + str(pawn1.get_position()))
pawn1.move((3, 6))
print("(3, 6)\t\t= " + str(pawn1.get_position()))
pawn1.move((3, 8))
print("(3, 8)\t\t= " + str(pawn1.get_position()))
pawn1.move((3, 10))
print("(3, 8)\t\t= " + str(pawn1.get_position()))
pawn1.move((3, 7))
print("(3, 8)\t\t= " + str(pawn1.get_position()))
pawn1.move((3, 10))
print("(3, 8)\t\t= " + str(pawn1.get_position()))

# VI) Test the replace method in Pawn
print("\nVI) Test the replace method in Pawn")
pawn1 = Pawn("pawn1", (3, 7), "white", "UP")
pawn1.replace(pawn2)
print("False\t\t= " + str(pawn1.is_piece_on_board()))
print("True\t\t= " + str(pawn2.is_piece_on_board()))
print("(None, None)\t= " + str(pawn1.get_position()))
print("(3, 7)\t\t= " + str(pawn2.get_position()))
pawn3.replace(pawn1)
print("True\t\t= " + str(pawn1.is_piece_on_board()))
print("False\t\t= " + str(pawn3.is_piece_on_board()))
print("(4, 2)\t\t= " + str(pawn1.get_position()))
print("(None, None)\t= " + str(pawn3.get_position()))
pawn1.replace(pawn2)
print("True\t\t= " + str(pawn1.is_piece_on_board()))
print("True\t\t= " + str(pawn2.is_piece_on_board()))
print("(4, 2)\t\t= " + str(pawn1.get_position()))
print("(3, 7)\t\t= " + str(pawn2.get_position()))

print("\n-------------------------------------------------------------------------------")
if pause:
    input()

# VII) Test the inherited constructor in King and its optional parameters
print("\nVII) Test the inherited constructor in King and its optional parameters")
try:
    king1 = King("king1", (0, 0), "taupe", "UP", (4, 4))
    print("King constructor appears to work correctly")
except:
    print("WARNING! Exception during King construction!")

try:
    king2 = King("king2", (3, 6), "black", "DOWN")
    print("Optional parameter in King constructor appears to work correctly")
except:
    king2 = King("king2", (3, 6), "black", "DOWN", (8, 8))
    print("WARNING! Optional parameter for King failed! Falling back to full constructor.")

if isinstance(king1, Chess_Piece):
    print("Kings are properly inheriting from Chess_Piece")
else:
    print("WARNING! Kings are not inheriting from Chess_Piece")

# VIII) Test the accessor methods of Chess_Piece in King
print("\nVIII) Test the inherited accessor methods of Chess_Piece in King")
print("king1\t\t= " + str(king1.get_ID()))
print("(0, 0)\t\t= " + str(king1.get_position()))
print("taupe\t\t= " + str(king1.get_color()))
print("UP\t\t= " + str(king1.get_direction()))
print("(4, 4)\t\t= " + str(king1.get_board_size()))
print("True\t\t= " + str(king1.is_piece_on_board()))
print("Valid moves?\t= " +
      ("WORKS!" if set(king1.get_valid_moves()) == set([(0, 1), (1, 1), (1, 0)]) else "Failed") +
      "\n\t\t" + str(king1.get_valid_moves()))
print()
print("king2\t\t= " + str(king2.get_ID()))
print("(3, 6)\t\t= " + str(king2.get_position()))
print("black\t\t= " + str(king2.get_color()))
print("DOWN\t\t= " + str(king2.get_direction()))
print("(8, 8)\t\t= " + str(king2.get_board_size()))
print("True\t\t= " + str(king2.is_piece_on_board()))
print("Valid moves?\t= " +
      ("WORKS!" if set(king2.get_valid_moves()) == set(
          [(3, 5), (2, 5), (2, 6), (2, 7), (3, 7), (4, 7), (4, 6), (4, 5)]) else "Failed") +
      "\n\t\t" + str(king2.get_valid_moves()))

if pause:
    input()

# IX) Test the inherited mutator methods of place and remove in King
print("\nIX) Test the inherited mutator methods of place and remove in King")
king1.place((2, 2))
print("(0, 0)\t\t= " + str(king1.get_position()))
king1.remove()
print("(None, None)\t= " + str(king1.get_position()))
king1.place((0, -1))
print("(None, None)\t= " + str(king1.get_position()))
king1.place((12, 5))
print("(None, None)\t= " + str(king1.get_position()))
king1.place((3, 1))
print("(3, 1)\t\t= " + str(king1.get_position()))

# X) Test the inherited mutator methods of move and take in King
print("\nX) Test the inherited mutator methods of move and take in King")
king1.take(pawn1)
print("--------------------------------")
print("Make sure pawn1 is not taken by king1 (king1 has a 4x4 board)")
print("True\t\t= " + str(pawn1.is_piece_on_board()))
print("(3, 1)\t\t= " + str(king1.get_position()))
print("--------------------------------")
king2.move((4, 3))
print("(3, 6)\t\t= " + str(king2.get_position()))
king2.move((3, 5))
print("(3, 5)\t\t= " + str(king2.get_position()))
king2.move((3, 4))
print("(3, 4)\t\t= " + str(king2.get_position()))
king2.move((3, 3))
print("(3, 3)\t\t= " + str(king2.get_position()))
king2.take(pawn1)
print("True\t\t= " + str(king2.is_piece_on_board()))
print("False\t\t= " + str(pawn1.is_piece_on_board()))
print("(4, 2)\t\t= " + str(king2.get_position()))

print("\n-------------------------------------------------------------------------------")
if pause:
    input()

# XI) Test the inherited constructor in Knight and its optional parameters
print("\nXI) Test the inherited constructor in Knight and its optional parameters")
try:
    knight1 = Knight("knight1", (1, 4), "green", "DOWN", (6, 6))
    print("Knight constructor appears to work correctly")
except:
    print("WARNING! Exception during Knight construction!")

try:
    knight2 = Knight("knight2", (3, 5), "white", "UP")
    print("Optional parameter in Knight constructor appears to work correctly")
except:
    knight2 = Knight("knight2", (3, 5), "white", "UP", (8, 8))
    print("WARNING! Optional parameter for Knight failed! Falling back to full constructor.")

if isinstance(knight1, Chess_Piece):
    print("Knights are properly inheriting from Chess_Piece")
else:
    print("WARNING! Knights are not inheriting from Chess_Piece")

# XII) Test the accessor methods of Chess_Piece in Knight
print("\nXII) Test the inherited accessor methods of Chess_Piece in Knight")
print("knight1\t\t= " + str(knight1.get_ID()))
print("(1, 4)\t\t= " + str(knight1.get_position()))
print("green\t\t= " + str(knight1.get_color()))
print("DOWN\t\t= " + str(knight1.get_direction()))
print("(6, 6)\t\t= " + str(knight1.get_board_size()))
print("True\t\t= " + str(knight1.is_piece_on_board()))
print("Valid moves?\t= " +
      ("WORKS!" if set(knight1.get_valid_moves()) == set([(3, 5), (3, 3), (2, 2), (0, 2)]) else "Failed") +
      "\n\t\t" + str(knight1.get_valid_moves()))
print()
print("knight2\t\t= " + str(knight2.get_ID()))
print("(3, 5)\t\t= " + str(knight2.get_position()))
print("white\t\t= " + str(knight2.get_color()))
print("UP\t\t= " + str(knight2.get_direction()))
print("(8, 8)\t\t= " + str(knight2.get_board_size()))
print("True\t\t= " + str(knight2.is_piece_on_board()))
print("Valid moves?\t= " +
      ("WORKS!" if set(knight2.get_valid_moves()) == set(
          [(4, 7), (5, 6), (5, 4), (4, 3), (2, 3), (1, 4), (1, 6), (2, 7)]) else "Failed") +
      "\n\t\t" + str(knight2.get_valid_moves()))

if pause:
    input()

# XIII) Test the inherited mutator methods of place and remove in Knight
print("\nXIII) Test the inherited mutator methods of place and remove in Knight")
knight2.place((2, 2))
print("(3, 5)\t\t= " + str(knight2.get_position()))
knight2.remove()
print("(None, None)\t= " + str(knight2.get_position()))
knight2.place((0, -1))
print("(None, None)\t= " + str(knight2.get_position()))
knight2.place((12, 5))
print("(None, None)\t= " + str(knight2.get_position()))
knight2.place((3, 5))
print("(3, 5)\t\t= " + str(knight2.get_position()))

# XIV) Test the inherited mutator methods of move and take in Knight
print("\nXIV) Test the inherited mutator methods of move and take in Knight")
knight2.take(king2)
print("--------------------------------")
print("Make sure king2 is not taken by knight2")
print("True\t\t= " + str(king2.is_piece_on_board()))
print("(3, 5)\t\t= " + str(knight2.get_position()))
print("--------------------------------")
knight2.take(knight1)
print("True\t\t= " + str(knight2.is_piece_on_board()))
print("False\t\t= " + str(knight1.is_piece_on_board()))
print("(1, 4)\t\t= " + str(knight2.get_position()))
knight2.move((0, 6))
print("(0, 6)\t\t= " + str(knight2.get_position()))
knight2.move((7, 0))
print("(0, 6)\t\t= " + str(knight2.get_position()))
knight2.move((2, 5))
print("(2, 5)\t\t= " + str(knight2.get_position()))
knight2.move((0, 4))
print("(0, 4)\t\t= " + str(knight2.get_position()))
knight2.move((1, 5))
print("(0, 4)\t\t= " + str(knight2.get_position()))
knight2.move((1, 6))
print("(1, 6)\t\t= " + str(knight2.get_position()))
knight2.move((2, 4))
print("(2, 4)\t\t= " + str(knight2.get_position()))
knight2.move((0, 5))
print("(0, 5)\t\t= " + str(knight2.get_position()))

print("\n-------------------------------------------------------------------------------")
if pause:
    input()

# XV) Test the inherited constructor in Bishop and its optional parameters
print("\nXV) Test the inherited constructor in Bishop and its optional parameters")
try:
    bishop1 = Bishop("bishop1", (3, 6), "invisible", "DOWN", (5, 7))
    print("Bishop constructor appears to work correctly")
except:
    print("WARNING! Exception during Bishop construction!")

try:
    bishop2 = Bishop("bishop2", (4, 3), "brown", "UP")
    print("Optional parameter in Bishop constructor appears to work correctly")
except:
    bishop2 = Bishop("bishop2", (4, 3), "brown", "UP", (8, 8))
    print("WARNING! Optional parameter for Bishop failed! Falling back to full constructor.")

if isinstance(knight1, Chess_Piece):
    print("Bishops are properly inheriting from Chess_Piece")
else:
    print("WARNING! Bishops are not inheriting from Chess_Piece")

# XVI) Test the accessor methods of Chess_Piece in Bishop
print("\nXVI) Test the inherited accessor methods of Chess_Piece in Bishop")
print("bishop1\t\t= " + str(bishop1.get_ID()))
print("(3, 6)\t\t= " + str(bishop1.get_position()))
print("invisible\t= " + str(bishop1.get_color()))
print("DOWN\t\t= " + str(bishop1.get_direction()))
print("(5, 7)\t\t= " + str(bishop1.get_board_size()))
print("True\t\t= " + str(bishop1.is_piece_on_board()))
print("Valid moves?\t= " +
      ("WORKS!" if set(bishop1.get_valid_moves()) == set([(2, 5), (4, 5), (1, 4), (0, 3)]) else "Failed") +
      "\n\t\t" + str(bishop1.get_valid_moves()))
print()
print("bishop2\t\t= " + str(bishop2.get_ID()))
print("(4, 3)\t\t= " + str(bishop2.get_position()))
print("brown\t\t= " + str(bishop2.get_color()))
print("UP\t\t= " + str(bishop2.get_direction()))
print("(8, 8)\t\t= " + str(bishop2.get_board_size()))
print("True\t\t= " + str(bishop2.is_piece_on_board()))
print("Valid moves?\t= " +
      ("WORKS!" if set(bishop2.get_valid_moves()) == set(
          [(0, 7), (1, 6), (7, 6), (2, 5), (6, 5), (3, 4), (5, 4), (3, 2), (5, 2), (2, 1), (6, 1), (1, 0),
           (7, 0)]) else "Failed") +
      "\n\t\t" + str(bishop2.get_valid_moves()))

if pause:
    input()

# XVII) Test the inherited mutator methods of place and remove in Bishop
print("\nXVII) Test the inherited mutator methods of place and remove in Bishop")
bishop2.place((2, 2))
print("(4, 3)\t\t= " + str(bishop2.get_position()))
bishop2.remove()
print("(None, None)\t= " + str(bishop2.get_position()))
bishop2.place((0, -1))
print("(None, None)\t= " + str(bishop2.get_position()))
bishop2.place((12, 5))
print("(None, None)\t= " + str(bishop2.get_position()))
bishop2.place((3, 5))
print("(3, 5)\t\t= " + str(bishop2.get_position()))

# XVIII) Test the inherited mutator methods of move and take in Bishop
print("\nXVIII) Test the inherited mutator methods of move and take in Bishop")
bishop1.take(knight2)
print("--------------------------------")
print("Make sure knight2 is not taken by bishop1")
print("True\t\t= " + str(knight2.is_piece_on_board()))
print("(3, 6)\t\t= " + str(bishop1.get_position()))
print("--------------------------------")
bishop1 = Bishop("bishop1", (4, 0), "red", "UP")
bishop2.move((0, 6))
print("(3, 5)\t\t= " + str(bishop2.get_position()))
bishop2.move((6, 2))
print("(6, 2)\t\t= " + str(bishop2.get_position()))
bishop2.take(bishop1)
print("False\t\t= " + str(bishop1.is_piece_on_board()))
print("True\t\t= " + str(bishop2.is_piece_on_board()))
print("(4, 0)\t\t= " + str(bishop2.get_position()))
bishop2.move((0, 4))
print("(0, 4)\t\t= " + str(bishop2.get_position()))
bishop2.move((0, 7))
print("(0, 4)\t\t= " + str(bishop2.get_position()))
bishop2.move((3, 7))
print("(3, 7)\t\t= " + str(bishop2.get_position()))
bishop2.move((2, 6))
print("(2, 6)\t\t= " + str(bishop2.get_position()))
bishop2.move((3, 5))
print("(3, 5)\t\t= " + str(bishop2.get_position()))

print("\n-------------------------------------------------------------------------------")
if pause:
    input()

# XIX) Test the inherited constructor in Rook and its optional parameters
print("\nXIX) Test the inherited constructor in Rook and its optional parameters")
try:
    rook1 = Rook("rook1", (0, 1), "blue", "UP", (4, 3))
    print("Rook constructor appears to work correctly")
except:
    print("WARNING! Exception during Rook construction!")

try:
    rook2 = Rook("rook2", (4, 3), "yellow", "DOWN")
    print("Optional parameter in Rook constructor appears to work correctly")
except:
    rook2 = Rook("rook2", (4, 3), "yellow", "DOWN", (8, 8))
    print("WARNING! Optional parameter for Rook failed! Falling back to full constructor.")

if isinstance(rook1, Chess_Piece):
    print("Rooks are properly inheriting from Chess_Piece")
else:
    print("WARNING! Rooks are not inheriting from Chess_Piece")

# XX) Test the accessor methods of Chess_Piece in Rook
print("\nXX) Test the inherited accessor methods of Chess_Piece in Rook")
print("rook1\t\t= " + str(rook1.get_ID()))
print("(0, 1)\t\t= " + str(rook1.get_position()))
print("blue\t\t= " + str(rook1.get_color()))
print("UP\t\t= " + str(rook1.get_direction()))
print("(4, 3)\t\t= " + str(rook1.get_board_size()))
print("True\t\t= " + str(rook1.is_piece_on_board()))
print("Valid moves?\t= " +
      ("WORKS!" if set(rook1.get_valid_moves()) == set([(0, 0), (0, 2), (1, 1), (2, 1), (3, 1)]) else "Failed") +
      "\n\t\t" + str(rook1.get_valid_moves()))
print()
print("rook2\t\t= " + str(rook2.get_ID()))
print("(4, 3)\t\t= " + str(rook2.get_position()))
print("yellow\t\t= " + str(rook2.get_color()))
print("DOWN\t\t= " + str(rook2.get_direction()))
print("(8, 8)\t\t= " + str(rook2.get_board_size()))
print("True\t\t= " + str(rook2.is_piece_on_board()))
print("Valid moves?\t= " +
      ("WORKS!" if set(rook2.get_valid_moves()) == set(
          [(5, 3), (6, 3), (7, 3), (3, 3), (2, 3), (1, 3), (0, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 2), (4, 1),
           (4, 0)]) else "Failed") +
      "\n\t\t" + str(rook2.get_valid_moves()))

if pause:
    input()

# XXI) Test the inherited mutator methods of place and remove in Rook
print("\nXXI) Test the inherited mutator methods of place and remove in Rook")
rook2.place((2, 2))
print("(4, 3)\t\t= " + str(rook2.get_position()))
rook2.remove()
print("(None, None)\t= " + str(rook2.get_position()))
rook2.place((0, -1))
print("(None, None)\t= " + str(rook2.get_position()))
rook2.place((12, 5))
print("(None, None)\t= " + str(rook2.get_position()))
rook2.place((3, 5))
print("(3, 5)\t\t= " + str(rook2.get_position()))

# XXII) Test the inherited mutator methods of move and take in Rook
print("\nXXII) Test the inherited mutator methods of move and take in Rook")
rook2.take(rook1)
print("--------------------------------")
print("Make sure rook1 is not taken by rook2")
print("True\t\t= " + str(rook1.is_piece_on_board()))
print("(3, 5)\t\t= " + str(rook2.get_position()))
print("--------------------------------")
rook2.move((0, 6))
print("(3, 5)\t\t= " + str(rook2.get_position()))
rook2.move((3, 3))
print("(3, 3)\t\t= " + str(rook2.get_position()))
rook2.move((0, 3))
print("(0, 3)\t\t= " + str(rook2.get_position()))
rook2.take(rook1)
print("False\t\t= " + str(rook1.is_piece_on_board()))
print("True\t\t= " + str(rook2.is_piece_on_board()))
print("(0, 1)\t\t= " + str(rook2.get_position()))
rook2.move((0, 7))
print("(0, 7)\t\t= " + str(rook2.get_position()))
rook2.move((7, 7))
print("(7, 7)\t\t= " + str(rook2.get_position()))
rook2.move((7, 3))
print("(7, 3)\t\t= " + str(rook2.get_position()))
rook2.move((3, 3))
print("(3, 3)\t\t= " + str(rook2.get_position()))

print("\n-------------------------------------------------------------------------------")
if pause:
    input()

# XXIII) Test the inherited constructor in Queen and its optional parameters
print("\nXXIII) Test the inherited constructor in Queen and its optional parameters")
try:
    queen1 = Queen("queen1", (2, 2), "grey", "UP", (5, 5))
    print("Queen constructor appears to work correctly")
except:
    print("WARNING! Exception during Queen construction!")

try:
    queen2 = Queen("queen2", (4, 3), "orange", "DOWN")
    print("Optional parameter in Queen constructor appears to work correctly")
except:
    queen2 = Queen("queen2", (4, 3), "orange", "DOWN", (8, 8))
    print("WARNING! Optional parameter for Queen failed! Falling back to full constructor.")

if isinstance(queen1, Rook):
    print("Queens are properly inheriting from Rook")
else:
    print("WARNING! Queens are not inheriting from Rook")

# XXIV) Test the accessor methods of Chess_Piece in Queen
print("\nXXIV) Test the inherited accessor methods of Chess_Piece in Queen")
print("queen1\t\t= " + str(queen1.get_ID()))
print("(2, 2)\t\t= " + str(queen1.get_position()))
print("grey\t\t= " + str(queen1.get_color()))
print("UP\t\t= " + str(queen1.get_direction()))
print("(5, 5)\t\t= " + str(queen1.get_board_size()))
print("True\t\t= " + str(queen1.is_piece_on_board()))
print("Valid moves?\t= " +
      ("WORKS!" if set(queen1.get_valid_moves()) == set(
          [(0, 0), (0, 4), (1, 1), (1, 3), (3, 1), (3, 3), (4, 0), (4, 4), (0, 2), (1, 2), (3, 2), (4, 2), (2, 0),
           (2, 1), (2, 3), (2, 4)]) else "Failed") +
      "\n\t\t" + str(queen1.get_valid_moves()))
print()
print("queen2\t\t= " + str(queen2.get_ID()))
print("(4, 3)\t\t= " + str(queen2.get_position()))
print("orange\t\t= " + str(queen2.get_color()))
print("DOWN\t\t= " + str(queen2.get_direction()))
print("(8, 8)\t\t= " + str(queen2.get_board_size()))
print("True\t\t= " + str(queen2.is_piece_on_board()))
print("Valid moves?\t= " +
      ("WORKS!" if set(queen2.get_valid_moves()) == set(
          [(0, 7), (1, 6), (7, 6), (2, 5), (6, 5), (3, 4), (5, 4), (3, 2), (5, 2), (2, 1), (6, 1), (1, 0), (7, 0),
           (5, 3), (6, 3), (7, 3), (3, 3), (2, 3), (1, 3), (0, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 2), (4, 1),
           (4, 0)]) else "Failed") +
      "\n\t\t" + str(queen2.get_valid_moves()))

if pause:
    input()

# XXV) Test the inherited mutator methods of place and remove in Queen
print("\nXXV) Test the inherited mutator methods of place and remove in Queen")
queen2.place((2, 2))
print("(4, 3)\t\t= " + str(queen2.get_position()))
queen2.remove()
print("(None, None)\t= " + str(queen2.get_position()))
queen2.place((0, -1))
print("(None, None)\t= " + str(queen2.get_position()))
queen2.place((12, 5))
print("(None, None)\t= " + str(queen2.get_position()))
queen2.place((7, 6))
print("(7, 6)\t\t= " + str(queen2.get_position()))

# XXVI) Test the inherited mutator methods of move and take in Queen
print("\nXXVI) Test the inherited mutator methods of move and take in Queen")
queen2.take(queen1)
print("--------------------------------")
print("Make sure queen1 is not taken by queen2")
print("True\t\t= " + str(queen1.is_piece_on_board()))
print("(7, 6)\t\t= " + str(queen2.get_position()))
print("--------------------------------")
queen2.move((0, 0))
print("(7, 6)\t\t= " + str(queen2.get_position()))
queen2.move((1, 6))
print("(1, 6)\t\t= " + str(queen2.get_position()))
queen2.move((4, 3))
print("(4, 3)\t\t= " + str(queen2.get_position()))
queen2.move((4, 4))
print("(4, 4)\t\t= " + str(queen2.get_position()))
queen2.take(queen1)
print("False\t\t= " + str(queen1.is_piece_on_board()))
print("True\t\t= " + str(queen2.is_piece_on_board()))
print("(2, 2)\t\t= " + str(queen2.get_position()))
queen2.move((4, 0))
print("(4, 0)\t\t= " + str(queen2.get_position()))
queen2.move((4, 8))
print("(4, 0)\t\t= " + str(queen2.get_position()))
queen2.move((0, 4))
print("(0, 4)\t\t= " + str(queen2.get_position()))
queen2.move((0, 0))
print("(0, 0)\t\t= " + str(queen2.get_position()))
queen2.move((6, 6))
print("(6, 6)\t\t= " + str(queen2.get_position()))
