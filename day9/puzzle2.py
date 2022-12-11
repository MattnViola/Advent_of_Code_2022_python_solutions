# Need to change to have 10 body pieces, 1 head, 8 body, and 1 tail.

def main():
    data = []
    tail_places = [(0,0)]

    with open('input.txt', 'r') as file:
        for line in file:
            line = line.rstrip('\n').split()
            line[1] = int(line[1])
            data.append(line)
    # Starting x,y position for body positions      
    body_pos = [(0,0)] * 10


    for move in data:
        # Iterate through repeated moves
        for _ in range(move[1]):
            # Move head part
            body_pos[0] = move_head(move[0], body_pos[0])
            # Iterate through body parts, check if they need to move
            for i in range(1,len(body_pos)):
                body_pos[i] = move_tail(body_pos[i - 1], body_pos[i])
            # Check if tail moved to a new place
            if not body_pos[9] in tail_places:
                tail_places.append(body_pos[9])
                
    print(len(tail_places))
    
            
           
def move_head(direction, pos):
    if direction == 'U': pos = (pos[0], pos[1] + 1)
    elif direction == 'D': pos = (pos[0], pos[1] - 1)
    elif direction == 'L': pos = (pos[0] - 1, pos[1])
    elif direction == 'R': pos = (pos[0] + 1, pos[1])
    return pos
    
# There is now the possibility for both x and y to be 2 positions away.    
def move_tail(head_pos, tail_pos):
    x_diff = abs(head_pos[0] - tail_pos[0])
    y_diff = abs(head_pos[1] - tail_pos[1])
    x = 1 if head_pos[0] > tail_pos[0] else -1
    y = 1 if head_pos[1] > tail_pos[1] else -1
    # Check for diagonal move
    if (x_diff == 2 and y_diff >= 1) or (x_diff >= 1 and y_diff == 2):
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

