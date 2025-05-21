def is_valid_chess_board(board):
    # Valid board positions (e.g., 1a to 8h)
    rows = ['1','2','3','4','5','6','7','8']
    cols = ['a','b','c','d','e','f','g']
    valid_positions = [r + c for r in rows for c in cols]

    # Valid piece names
    valid_pieces = [
        'wpawn', 'wrook', 'wknight', 'wbishop', 'wqueen', 'wking',
        'bpawn', 'brook', 'bknight', 'bbishop', 'bqueen', 'bking'
    ]

    # Counters
    white_king = 0
    black_king = 0

    for position, piece in board.items():
        if position not in valid_positions:
            print(f"Invalid position: {position}")
            return False
        if piece not in valid_pieces:
            print(f"Invalid piece: {piece}")
            return False
        if piece == 'wking':
            white_king += 1
        if piece == 'bking':
            black_king += 1

    if white_king != 1 or black_king != 1:
        print("There must be exactly one white king and one black king.")
        return False

    return True

# Example chess board dictionary
chess_board = {
    '1a': 'wrook',
    '1b': 'wknight',
    '1c': 'wbishop',
    '1d': 'wqueen',
    '1e': 'wking',
    '1f': 'wbishop',
    '1g': 'wknight',
    '1h': 'wrook',
    '8e': 'bking',
    '7a': 'bpawn'
}

# Validate board
if is_valid_chess_board(chess_board):
    print("✅ Chess board is valid!")
else:
    print("❌ Chess board is invalid.")
