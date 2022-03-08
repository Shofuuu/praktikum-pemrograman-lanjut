#!/usr/bin/python3

"""
    SOAL 1
    Melengkapi tabel catur
"""

board = []
chess = ['\u265B', '\u265C', '\u265D', '\u265A', '\u265E', '\u265F']
inside_row = [1, 4, 2, 0, 3, 2, 4, 1]

for x in range(8):
    row = [' ' for i in range(8)]
    board.append(row)

for x in range(8):
    # fill white row
    board[0][x] = chr(ord(chess[inside_row[x]])-6)
    board[1][x] = chr(ord(chess[5])-6)
    
    # fill black row
    board[7][x] = chess[inside_row[x]]
    board[6][x] = chess[5]

for x in range(8):
    print(board[x])