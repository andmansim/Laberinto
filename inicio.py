maze = [['S', 'X', 'X', 'X', 'X'], 
        ['', 'X', '', '', ''],
        ['', 'X', '', 'X', ''],
        ['', '', '', 'X', ''], 
        ['X', 'X', 'X', 'X', 'E']]
# S = start E = exit X = wall
wall = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (4,3), (5,0), (5,1), (5,2), (5,3))
exit = ((5,4))
start = ((0,0))