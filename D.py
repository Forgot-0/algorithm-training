board = [list(input()) for _ in range(8)]


for i in range(8):
    for j in range(8):
        piece = board[i][j]

        if piece == "R":
            for n in range(1, j+1):
                if board[i][j-n] not in ['R', 'B']:
                    board[i][j-n] = '.'
                else:
                    break
            
            for n in range(1, 8-j):
                if board[i][j+n] not in ['R', 'B']:
                    board[i][j+n] = '.'
                else:
                    break

            for n in range(1, i+1):
                if board[i-n][j] not in ['R', 'B']:
                    board[i-n][j] = '.'
                else:
                    break

            for n in range(1, 8-i):
                if board[i+n][j] not in ['R', 'B']:
                    board[i+n][j] = '.'
                else:
                    break
        elif piece == 'B':
            
            row, col = i-1, j+1
            while row >= 0 and col < 8:
                if board[row][col] not in ['R', 'B']:
                    board[row][col] = '.'
                else:
                    break
                row -= 1
                col += 1

            row, col = i + 1, j + 1
            while row < 8 and col < 8:
                if board[row][col] not in ['R', 'B']:
                    board[row][col] = '.'
                else:
                    break
                row += 1
                col += 1
            
            row, col = i - 1, j - 1
            while row >= 0 and col >= 0:
                if board[row][col] not in ['R', 'B']:
                    board[row][col] = '.'
                else:
                    break
                row -= 1
                col -= 1
            
            row, col = i + 1, j - 1
            while row < 8 and col >= 0:
                if board[row][col] not in ['R', 'B']:
                    board[row][col] = '.'
                else:
                    break
                row += 1
                col -= 1



print(sum(stroka.count('*') for stroka in board))