import gui

l = [[2, 0, 0, 0, 1, 0, 0, 6, 0],
     [0, 3, 8, 0, 0, 2, 0, 0, 0],
     [0, 1, 0, 9, 3, 6, 0, 2, 0],
     [1, 0, 0, 2, 8, 0, 0, 3, 0],
     [4, 8, 0, 0, 0, 0, 0, 7, 2],
     [0, 6, 0, 0, 4, 5, 0, 0, 9],
     [0, 7, 0, 4, 9, 8, 0, 1, 0],
     [0, 0, 0, 7, 0, 0, 4, 9, 0],
     [0, 4, 0, 0, 2, 0, 0, 0, 7]]

s1 = gui.sudoku(l)

s1.play()

