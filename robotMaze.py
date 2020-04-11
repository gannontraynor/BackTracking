
board = [["_","#","#","#","_","_","G"],
         ["_","_","#","_","_","#","#"],
         ["_","_","_","_","_","#","#"],
         ["_","_","_","_","_","#","#"],
         ["_","_","_","_","_","#","#"],
         ["_","_","_","_","_","#","#"],
         ["S","_","_","_","_","#","#"]]

def look(x,y):
## make a copy of the board so each robot can keep track of spaces visited. 
    visited = board
##check for the goal
    if board[x][y] == "G":
        print ('found at ' + str(x) + ", " + str(y))
        return True
##check for walls
    elif board[x][y] == "#":
        return False
##check to see it it has been visited
    elif visited[x][y] == "X":
        return False
##mark next open space as visited
    visited[x][y] = "X"

##recursively call look until the robot has found the goal, prioritizing
##turingin left, to simulate the theory
##that you can place your hand on the left wall and you will beat any maze.
##This code will follow one path until completion or it hits  a wall,
##then will go back to the next point with multiple positions then go from there and so on.
    
    if ((x > 0 and look(x-1, y)) or (y < len(board)-1 and look(x,y+1))
        or (x < len(board)-1 and look(x+1, y)) or (y > 0 and look(x, y-1))):
        return (x,y)

    return False

def robot(x):
    look(0,0)
        

robot(1)
    
