from random import randint

possibles = [1,2,3,4,5,6,7,8,9]

sudokuBox = [
    [-1,2,-1,-1,-1,4,3,-1,-1],
    [9,-1,-1,-1,2,-1,-1,-1,8],
    [-1,-1,-1,6,-1,9,-1,5,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,1],
    [-1,7,2,5,-1,3,6,8,-1],
    [6,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,8,-1,2,-1,5,-1,-1,-1],
    [1,-1,-1,-1,9,-1,-1,-1,3],
    [-1,-1,9,8,-1,-1,-1,6,-1]
]

def getArrays(target, boxes):
    return

def backTrack(n, m, currBox):
    
    print("State of box: ".join(str(x) for x in currBox))
    probs = possibles
    
    row = currBox[n]
    column = [0,0,0,0,0,0,0,0,0]

    rowCount = 0
    # Get Column
    for i in range(0, len(currBox)):
       
        column[rowCount] = currBox[i][m]
        rowCount += 1

    possibles_toRemove = list(set(row + column))
    possibles_toRemove.remove(-1)

    for i in range(len(possibles_toRemove)):
        try:
            probs.remove(possibles_toRemove[i])
        except:
            pass

    # Pick
    if len(probs) != 0:
        chosen = probs[randint(0, len(probs) - 1)]
        currBox[n][m] = chosen
        
        if m + 1 > 9:
            backTrack(n+1, 0, currBox)
        else:
            backTrack(n, m+1, currBox)
    else:
        if m - 1 < 0:
            backTrack(n-1, m, currBox)
        else:
            backTrack(n, m-1, currBox)
        

backTrack(0,0, sudokuBox)
# print(solve(0, full, False, False))
# solve_Caller(0, 0, sudokuBox, possibles, False, False)