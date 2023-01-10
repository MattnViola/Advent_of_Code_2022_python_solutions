import numpy as np

grid = open('input.txt','r').read()
grid = list(map(list, grid.split('\n')))

# Records blizzard locations in the directions.
up,down,right,left = [],[],[],[]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        match grid[i][j]:
            case '^':
                up.append((i, j))
            case 'v':
                down.append((i,j))
            case '>':
                right.append((i,j))
            case '<':
                left.append((i,j))

up,down,right,left = np.array(up),np.array(down),np.array(right),np.array(left)
              
bliz_over_time = [[up,down,right,left]]

# Index 0 dimensions
dim = (len(grid) - 1,len(grid[0]) - 1)

for i in range(len(grid[0])):
    if grid[0][i] == '.':
        start = (0,i)
        
for i in range(len(grid[-1])):
    if grid[-1][i] == '.':
        end = ((len(grid) - 1, i))
        


# routes through graph, checks if there is going to be a blizzard there next turn. It can go backwards. Records best time
def route_search(bliz_over_time, pos, goal):
    global dim
    queue = [pos]
    t = 0
    while queue:
        # Down, right, stay, up, left, 
        possible_routes = [(-1,0),(0,1),(0,0),(1,0),(0,-1)]
        # Adds the surroundings of each node in queue, as well as the node itself
        new_queue = [(q[0]+possible_routes[r][0], q[1] + possible_routes[r][1]) for q in queue for r in range(len(possible_routes))]
        queue, t = [], t + 1

        if t == len(bliz_over_time):
            bliz_over_time.append(move_blizzards(bliz_over_time[t-1]))
        set_bliz = set()
        for x in bliz_over_time[t]:
            set_bliz.update(map(tuple,x))
        # Checks new queue nodes validity / if it's the goal
        for ny,nx in new_queue:
            if (ny,nx) == goal:
                print(t)
                return         
            if (ny <= 0 or ny >= dim[0] or nx <= 0 or nx >= dim[1]) and ((ny,nx) != (0,1) and (ny,nx) != goal):
                continue
            if (ny,nx) not in set_bliz:
                queue.append((ny,nx))
                


    
 
# Moves the blizzards one tile and records it in bliz_over_time
def move_blizzards(bliz):
    global dim
    y,x = dim
    up,down,right,left = [np.copy(direction) for direction in bliz]
    
    up += (-1,0)
    up[up == (0,...)] = y - 1
    
    down += (1,0)
    down[down == (y,...)] = 1
    
    right += (0,1)
    right[right == (...,x)] = 1
    
    left += (0,-1)
    left[left == (...,0)] = x - 1
    
    return [up,down,right,left]
    
                
route_search(bliz_over_time,start,end)


        