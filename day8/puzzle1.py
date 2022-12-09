# Need to input the grid in a matrix and then see if it's taller than all other trees to a side of it.

# Solution is how many visible trees

grid = []

def main():
    with open('input.txt', 'r') as file:
        # Input into 2d list
        i = 0
        for line in file:
            grid.append(list(map(int, list(line.rstrip('\n')))))
            i += 1
        # Check if tree is visible from side
        visible = 0
        l_highest = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                x = grid[i][j]
                # Checking from left
                if x > l_highest:
                    l_highest = x
                    visible += 1
                    continue
                # If not from left, checking from right
                if r_check(grid, i, j):
                    visible += 1
                    continue
                # If not from right, checking from up
                if u_check(grid, i, j):
                    visible += 1
                    continue
                # if not from up, checking from down
                if d_check(grid, i, j):
                    visible += 1
                    continue
            l_highest = -1
        print(visible)
        
                
def r_check(grid, row, column):
    # Checking from the left
    r_highest = -1
    vis = False
    for i in range(1, len(grid[0]) + 1):
        x = grid[row][-i]
        if column + i == len(grid[0]):
            if grid[row][column] > r_highest:
                vis = True
                break
            else:
                break
        if x > r_highest:
            r_highest = x
    return vis
def u_check(grid, row, column):
    # Checking from above
    a_highest = -1
    vis = False
    for i in range(len(grid)):
        x = grid[i][column]
        if i == row:
            if grid[row][column] > a_highest:
                vis = True
                break 
            else:
                break
        if x > a_highest:
            a_highest = x
    return vis
    
def d_check(grid, row, column):
    # Checking from below
    b_highest = -1
    vis = False
    for i in range(1,len(grid) + 1):
        x = grid[-i][column]
        if i + row == len(grid):
            if grid[row][column] > b_highest:
                vis = True
                break
            else:
                break
        if x > b_highest:
            b_highest = x
    return vis
    
    
    
if __name__ == '__main__':
    main()
    
    
# If there's a >= height before, then dont have to iterate through. 