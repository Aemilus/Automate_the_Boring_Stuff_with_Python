"""
Write a function that takes a dictionary argument and returns True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king.
Each player can only have at most 16 pieces, at most 8 pawns,
and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'.
"""

import pprint


def validate_chess_board(_chess_board):
    _validations = list()
    _validations.append(_validate_chess_pieces_color(_chess_board))
    _validations.append(_validate_chess_pieces_count(_chess_board))
    _validations.append(_validate_chess_pawns_count(_chess_board))
    _validations.append(_validate_chess_piece_count(_chess_board, 'K', 1))

    return False not in _validations


def _validate_chess_pieces_color(_chess_board):
    _unexpected_chess_colors = {'white', 'black'}
    for _player, _player_board in _chess_board.items():
        _unexpected_chess_colors.remove(_player_board['color'])
    if _unexpected_chess_colors:
        print("The colors of the players' pieces are invalid.")
        return False
    else:
        print("The colors of the players' pieces are valid.")
        return True


def _validate_chess_pieces_count(_chess_board):
    for _player, _player_board in _chess_board.items():
        if len(_player_board['pieces']) > 16:
            print("The count of the players' pieces is invalid.")
            return False
        else:
            print("The count of the players' pieces is valid.")
            return True


def _validate_chess_piece_count(_chess_board, _piece, _max_count):
    _pieces_name = {'K': 'king'}
    for _player, _player_board in _chess_board.items():
        _count = 0
        for _piece_info in _player_board['pieces']:
            _count += int(_piece in _piece_info[0])
        if _count > _max_count:
            print(f"The {_pieces_name[_piece]}s count is invalid.")
            return False
        else:
            print(f"The {_pieces_name[_piece]}s count is valid.")
            return True


def _validate_chess_pawns_count(_chess_board):
    for _player, _player_board in _chess_board.items():
        _count = 0
        for _piece_info in _player_board['pieces']:
            # if the piece is a pawn then the convention is to just note its position
            # example: 'e5' means a pawn is on e5 square on the chess board
            _count += int(len(_piece_info) < 3)
        if _count > 8:
            print("The pawns count is invalid.")
            return False
        else:
            print("The pawns count is valid.")
            return True


if __name__ == '__main__':
    print("\n--- chess board ---")
    chess_board = {
        'player1': {
            'color': 'white',
            'pieces': ['e5', 'Ka2', 'Bd7'],

        },
        'player2': {
            'color': 'black',
            'pieces': ['e5', 'Kh3'],
        },
    }
    pprint.pprint(chess_board)

    print("\n--- validate chess board ---")
    print('validation result:', validate_chess_board(chess_board))
