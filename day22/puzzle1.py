

def main():
    board = []
    instructions = []
    
    with open('adventofcode\day22\\board.txt','r') as file:
        for line in file:
            board.append(list(line.rstrip('\n')))

    with open('adventofcode\day22\instructions.txt','r') as file:
        x = []
        for y in file.read():
            if y.isnumeric():
                x.append(y)
            else:
                instructions.append(int(''.join(x)))
                x.clear()
                instructions.append(y)

    # Set player down
    for i in range(len(board[0])):
        if board[0][i] == '.':
            # y,x
            current = (0,i)
            break
        
    # 0,1,2,3 R D L U
    direction = 0
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    for i in instructions:
        if type(i) == int:
            for _ in range(i):
                # dest : destination
                dest = next_place(direction, current, board)
                if dest:
                    current = dest
                else:
                    break
        else:
            # Changing direction
            if i == 'L':
                direction = (direction - 1) % 4
            elif i == 'R':
                direction = (direction + 1) % 4

    print(1000 * (current[0] + 1) + 4 * (current[1]+ 1) + direction)

def next_place(direction, current, board):
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    dir_y, dir_x = directions[direction]
    new_y, new_x = current[0] + dir_y, current[1] + dir_x

    # The wraparound
    try:
        x = board[new_y][new_x]
        if x == ' ' or dest[0] < 0 or dest[1] < 0:
            dest = wrap_around(new_y,new_x,dir_y,dir_x,board)
    except:
        dest = wrap_around(new_y,new_x, dir_y, dir_x, board)
    
    # Check for wall
    if board[dest[0]][dest[1]] == '#':
        return None
    return dest

def wrap_around(new_y,new_x,dir_y,dir_x,board):
    while True:
        new_y, new_x = new_y - dir_y, new_x - dir_x
        try:
            z = board[new_y][new_x]
            if z == ' ' or new_y == 0 or new_x == 0:
                return new_x + dir_x, new_y + dir_y
        except:
            return new_x + dir_x, new_y + dir_y
                

main()
