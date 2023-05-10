import unittest
from unittest.mock import patch, Mock
import chess_engine
import ai_engine
from Piece import Knight, Rook, Bishop, Queen, King, Pawn
from enums import Player


class TestGame(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName=methodName)
        self.game = chess_engine.game_state()

    def test_uni_knight_get_valid_peaceful_moves_in_empty_board_knight_in_the_middle(self):
        self.game.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
        # add the test_knight piece at its position
        test_knight = Knight('n', 3, 4, Player.PLAYER_1)
        self.game.board[3][4] = test_knight
        knight_moves = test_knight.get_valid_peaceful_moves(self.game)
        valid_peaceful_moves = [(1, 3), (1, 5), (2, 2), (2, 6),
                                (4, 2), (4, 6), (5, 5), (5, 3)]
        # Test that the knight can move to 8 different squares
        self.assertEqual(knight_moves, valid_peaceful_moves)

    def test_uni_knight_get_valid_peaceful_moves_in_empty_board_knight_in_the_corner(self):
        self.game.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
        # add the test_knight piece at its position
        test_knight = Knight('n', 0, 0, Player.PLAYER_1)
        self.game.board[0][0] = test_knight
        # Define the expected valid and peaceful moves for the knight
        valid_peaceful_moves = [(1, 2), (2, 1)]
        # Test that the knight can move to 2 different squares
        self.assertEqual(test_knight.get_valid_peaceful_moves(self.game), valid_peaceful_moves)

    def test_uni_knight_get_valid_peaceful_moves_in_empty_board_knight_in_the_edge(self):
        self.game.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
        # add the test_knight piece at its position
        test_knight = Knight('n', 0, 4, Player.PLAYER_1)
        self.game.board[0][4] = test_knight
        # Define the expected valid and peaceful moves for the knight
        valid_peaceful_moves = [(1, 2), (1, 6), (2, 5), (2, 3)]
        # Test that the knight can move to 4 different squares
        self.assertEqual(test_knight.get_valid_peaceful_moves(self.game), valid_peaceful_moves)

    def test_uni_knight_get_valid_piece_takes_in_empty_board_knight_in_the_middle(self):
        self.game.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
        # add the test_knight piece at its position
        test_knight = Knight('n', 3, 4, Player.PLAYER_1)
        self.game.board[3][4] = test_knight
        # Define the expected squares that the knight can attack
        valid_piece_takes = []
        # Test that the knight cannot attack any pieces
        self.assertEqual(test_knight.get_valid_piece_takes(self.game), valid_piece_takes)

    def test_uni_knight_get_valid_piece_takes_in_board_not_empty_knight_in_the_corner(self):
        # create an empty board
        self.game.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
        # add the test_knight piece at its position
        test_knight = Knight('n', 0, 0, Player.PLAYER_1)
        self.game.board[0][0] = test_knight
        # add two enemy pieces in valid take positions
        enemy1 = Knight('n', 2, 1, Player.PLAYER_2)
        enemy2 = Knight('n', 1, 2, Player.PLAYER_2)
        self.game.board[2][1] = enemy1
        self.game.board[1][2] = enemy2
        # Define the expected squares that the knight can attack
        valid_piece_takes = [(1, 2), (2, 1)]
        # Test that the knight can take the two enemy pieces
        self.assertEqual(test_knight.get_valid_piece_takes(self.game), valid_piece_takes)

    def test_uni_knight_get_valid_piece_takes_in_board_not_empty_knight_in_the_middle(self):
        # create an empty board
        self.game.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
        # add the test_knight piece at its position
        test_knight = Knight('n', 3, 4, Player.PLAYER_1)
        self.game.board[3][4] = test_knight
        # add two enemy pieces in valid take positions
        enemy1 = Knight('n', 5, 5, Player.PLAYER_2)
        enemy2 = Knight('n', 5, 3, Player.PLAYER_2)
        self.game.board[5][5] = enemy1
        self.game.board[5][3] = enemy2
        # Define the expected squares that the knight can attack
        valid_piece_takes = [(5, 5), (5, 3)]
        # Test that the knight can take the two enemy pieces
        self.assertEqual(test_knight.get_valid_piece_takes(self.game), valid_piece_takes)

    def test_integration_get_valid_piece_moves(self):
        self.game.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
        # add the test_knight piece at its position
        test_knight = Knight('n', 3, 4, Player.PLAYER_1)
        self.game.board[3][4] = test_knight
        # add two enemy pieces in valid take positions
        enemy1 = Knight('n', 5, 5, Player.PLAYER_2)
        enemy2 = Knight('n', 5, 3, Player.PLAYER_2)
        self.game.board[5][5] = enemy1
        self.game.board[5][3] = enemy2
        # Define the expected squares that the knight can attack
        valid_piece_moves = [(1, 3), (1, 5), (2, 2), (2, 6),
                             (4, 2), (4, 6), (5, 5), (5, 3)]
        # Test that the knight can take the two enemy pieces
        self.assertEqual(test_knight.get_valid_piece_moves(self.game), valid_piece_moves)

    def test_integration_evaluate_board(self):
        self.game.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
        # set up the board with some pieces
        self.game.board[0][0] = Rook('r', 0, 0, Player.PLAYER_1)
        self.game.board[1][1] = Knight('n', 1, 1, Player.PLAYER_1)
        self.game.board[2][2] = Bishop('b', 2, 2, Player.PLAYER_1)
        self.game.board[3][3] = Queen('q', 3, 3, Player.PLAYER_1)
        self.game.board[4][4] = King('k', 4, 4, Player.PLAYER_1)
        self.game.board[5][5] = Bishop('b', 5, 5, Player.PLAYER_1)
        self.game.board[6][6] = Knight('n', 6, 6, Player.PLAYER_1)
        self.game.board[7][7] = Rook('r', 7, 7, Player.PLAYER_1)
        self.game.board[0][7] = Rook('r', 0, 7, Player.PLAYER_2)
        self.game.board[1][6] = Knight('n', 1, 6, Player.PLAYER_2)
        self.game.board[2][5] = Bishop('b', 2, 5, Player.PLAYER_2)
        self.game.board[3][4] = Queen('q', 3, 4, Player.PLAYER_2)
        self.game.board[4][3] = King('k', 4, 3, Player.PLAYER_2)
        self.game.board[5][2] = Bishop('b', 5, 2, Player.PLAYER_2)
        self.game.board[6][1] = Knight('n', 6, 1, Player.PLAYER_2)
        self.game.board[7][0] = Rook('r', 7, 0, Player.PLAYER_2)
        # create an evaluation function
        evaluator = ai_engine.chess_ai()
        # evaluate the board for player 1
        player_1_score = evaluator.evaluate_board(self.game, Player.PLAYER_1)
        # evaluate the board for player 2
        player_2_score = evaluator.evaluate_board(self.game, Player.PLAYER_2)
        # check that the scores are equal and opposite
        self.assertEqual(player_1_score, -player_2_score)
        # check that the total score is zero
        self.assertEqual(player_1_score + player_2_score, 0)

    def test_system_mate_fools(self):
        # place a king and a queen in checkmate position for player 1
        self.game.board[0][0] = Rook('r', 0, 0, Player.PLAYER_1)
        self.game.board[0][1] = Knight('n', 0, 1, Player.PLAYER_1)
        self.game.board[0][2] = Bishop('b', 0, 2, Player.PLAYER_1)
        self.game.board[0][3] = Queen('q', 0, 3, Player.PLAYER_1)
        self.game.board[0][4] = King('k', 0, 4, Player.PLAYER_1)
        self.game.board[0][5] = Bishop('b', 0, 5, Player.PLAYER_1)
        self.game.board[0][6] = Knight('n', 0, 6, Player.PLAYER_1)
        self.game.board[0][7] = Rook('r', 0, 7, Player.PLAYER_1)
        self.game.board[1][0] = Pawn('p', 1, 0, Player.PLAYER_1)
        self.game.board[1][1] = Pawn('p', 1, 1, Player.PLAYER_1)
        self.game.board[1][2] = Pawn('p', 1, 2, Player.PLAYER_1)
        self.game.board[1][3] = Pawn('p', 1, 3, Player.PLAYER_1)
        self.game.board[1][3] = Pawn('p', 1, 4, Player.PLAYER_1)
        self.game.board[1][5] = Pawn('p', 1, 5, Player.PLAYER_1)
        self.game.board[1][6] = Pawn('p', 1, 6, Player.PLAYER_1)
        self.game.board[1][7] = Pawn('p', 1, 7, Player.PLAYER_1)
        self.game.board[7][0] = Rook('r', 7, 0, Player.PLAYER_2)
        self.game.board[7][1] = Knight('n', 7, 1, Player.PLAYER_2)
        self.game.board[7][2] = Bishop('b', 7, 2, Player.PLAYER_2)
        self.game.board[7][3] = Queen('q', 7, 3, Player.PLAYER_2)
        self.game.board[7][4] = King('k', 7, 4, Player.PLAYER_2)
        self.game.board[7][5] = Bishop('b', 7, 5, Player.PLAYER_2)
        self.game.board[7][6] = Knight('n', 7, 6, Player.PLAYER_2)
        self.game.board[7][7] = Rook('r', 7, 7, Player.PLAYER_2)
        self.game.board[6][0] = Pawn('p', 6, 0, Player.PLAYER_2)
        self.game.board[6][1] = Pawn('p', 6, 1, Player.PLAYER_2)
        self.game.board[6][2] = Pawn('p', 6, 2, Player.PLAYER_2)
        self.game.board[6][3] = Pawn('p', 6, 3, Player.PLAYER_2)
        self.game.board[6][4] = Pawn('p', 6, 4, Player.PLAYER_2)
        self.game.board[6][5] = Pawn('p', 6, 5, Player.PLAYER_2)
        self.game.board[6][6] = Pawn('p', 6, 6, Player.PLAYER_2)
        self.game.board[6][7] = Pawn('p', 6, 7, Player.PLAYER_2)

        self.game.move_piece((6, 4), (4, 4), False)
        self.game.move_piece((1, 3), (3, 3), False)
        self.game.move_piece((6, 6), (4, 6), False)
        self.game.move_piece((0, 5), (4, 1), False)

        # black player wins
        self.assertEqual(self.game.checkmate_stalemate_checker(), 0)
