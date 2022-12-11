# Need to have a tail follow a head through a grid, and report the amount of spaces a tail touched.
# If head gets more than 1 space away, tail follows
# Head can go over tail
def main():
    data = []
    tail_places = [(0,0)]

    with open('input.txt', 'r') as file:
        for line in file:
            line = line.rstrip('\n').split()
            line[1] = int(line[1])
            data.append(line)
    # Starting x,y position for head and tail        
    head_pos = (0,0)
    tail_pos = (0,0)


    for move in data:
        for i in range(move[1]):
            # Move head and check for tail following
            head_pos = move_head(move[0], head_pos)
            tail_pos = move_tail(head_pos, tail_pos)
            if not tail_pos in tail_places:
                tail_places.append(tail_pos)
    print(len(tail_places))
    
            
           
def move_head(direction, pos):
    if direction == 'U': pos = (pos[0], pos[1] + 1)
    elif direction == 'D': pos = (pos[0], pos[1] - 1)
    elif direction == 'L': pos = (pos[0] - 1, pos[1])
    elif direction == 'R': pos = (pos[0] + 1, pos[1])
    return pos
    
def move_tail(head_pos, tail_pos):
    x_diff = abs(head_pos[0] - tail_pos[0])
    y_diff = abs(head_pos[1] - tail_pos[1])
    x = 1 if head_pos[0] > tail_pos[0] else -1
    y = 1 if head_pos[1] > tail_pos[1] else -1
    # Check for diagonal move
    if (x_diff == 2 and y_diff == 1) or (x_diff == 1 and y_diff == 2):
           tail_pos = (tail_pos[0] + x, tail_pos[1] + y)
    # Check for horizontal move
    elif x_diff == 2:
        tail_pos = (tail_pos[0] + x, tail_pos[1])
    # Check for vertical move
    elif y_diff == 2:
        tail_pos = (tail_pos[0], tail_pos[1] + y)
    return tail_pos


if __name__ == '__main__':
    main()

