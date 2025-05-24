def is_valid_chess_board(board):
    piece_counts = {'bking': 0, 'wking': 0, 'bqueen': 0, 'wqueen': 0,
                    'bbishop': 0, 'wbishop': 0, 'bknight': 0, 'wknight': 0,
                    'brook': 0, 'wrook': 0, 'bpawn': 0, 'wpawn': 0}
    valid_spaces = [str(i) + str(j) for i in range(1, 9) for j in 'abcdefgh']

    for space, piece in board.items():
        if space not in valid_spaces:
            return False
        if piece[0] not in ['b', 'w']:
            return False
        piece_type = piece[1:]
        if piece_type not in ['king', 'queen', 'bishop', 'knight', 'rook', 'pawn']:
            return False
        piece_counts[piece] += 1

    if piece_counts['bking'] != 1 or piece_counts['wking'] != 1:
        return False
    if piece_counts['bpawn'] > 8 or piece_counts['wpawn'] > 8:
        return False
    if sum([count for piece, count in piece_counts.items() if piece[1:] == 'king']) != 2:
        return False

    return True

def main():
    board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
    print(is_valid_chess_board(board))

if _name_ == "_main_":
    main()
