# Need to put the trees in the same 2d list, and count the amount of visible trees in each direction, this includes the trees that blocks the view.
# Then, need to multiply the visible trees from each direction, a*b*l*r

grid = []
vis_score = []
def main():
    with open('input.txt', 'r') as file:
        # Input into 2d list
        for line in file:
            grid.append(list(map(int, list(line.rstrip('\n')))))
            
            
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            l = visible_l(grid, i, j)
            r = visible_r(grid, i, j)
            a = visible_a(grid, i, j)
            b = visible_b(grid, i, j)
            vis_score.append(l*r*a*b)
            
    print(max(vis_score))
def visible_l(grid, row, column):
    score = 0
    height = grid[row][column]
    for i in range(1, len(grid[row])):
        if column - i < 0:
            break
        if grid[row][column - i] >= height:
            score += 1
            break
        score += 1
    return score
        
def visible_r(grid, row, column):
    score = 0
    height = grid[row][column]
    for i in range(1, len(grid[row])):
        if column + i == len(grid[row]):
            break
        if grid[row][column + i] >= height:
            score += 1
            break
        score += 1
    return score

def visible_a(grid, row, column):
    score = 0
    height = grid[row][column]
    for i in range(1, len(grid)):
        if row - i < 0:
            break
        if grid[row - i][column] >= height:
            score += 1
            break
        score += 1
    return score    
    
def visible_b(grid, row, column):
    score = 0
    height = grid[row][column]
    for i in range(1, len(grid)):
        if row + i == len(grid):
            break
        if grid[row + i][column] >= height:
            score += 1
            break
        score += 1
    return score      





if __name__ == '__main__':
    main()