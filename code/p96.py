# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:41:55 2018

@author: lamwa
"""

import numpy as np

FULL = set(i for i in range(1, 10))

def dfs(board, i_p, rows, cols, chunks):
    global ans
    if i_p == len(pos[0]):
        ans += board[0][0] * 100 + board[0][1] * 10 + board[0][2]
        return None
    x, y = pos[0][i_p], pos[1][i_p]
    pots = rows[x] & cols[y] & chunks[x // 3][y // 3]
    for pot in pots:
        e = set([pot])
        rows[x] -= e
        cols[y] -= e
        chunks[x // 3][y // 3] -= e
        board[x, y] = pot
        dfs(board, i_p + 1, rows, cols, chunks)
        board[x, y] = 0
        rows[x] |= e
        cols[y] |= e
        chunks[x // 3][y // 3] |= e
    return None

with open('p096_sudoku.txt') as f:
    lines =  f.readlines()

boards = list()
for i in range(len(lines) // 10):
    boards.append(np.array([[int(c) for c in line.strip()] for line in lines[i * 10 + 1 : (i + 1) * 10]]))

ans = 0
for board in boards:
    pos = np.where(board == 0)

    rows = [set(num for num in range(1, 10) if num not in board[i, :]) for i in range(9)]
    cols = [set(num for num in range(1, 10) if num not in board[:, j]) for j in range(9)]
    chunks = [[set(num for num in range(1, 10) if num not in board[i * 3 : i * 3 + 3, j * 3 : j * 3 + 3]) for j in range(3)] for i in range(3)]
    
    dfs(board, 0, rows, cols, chunks)

print(ans)