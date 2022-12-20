# Now simulate the sand with an infinite floor 2 levels below lowest,
# And find how much sand it takes to block origin

def main():

    with open('input.txt','r') as file:
        data = [line.rstrip('\n').split(' -> ') for line in file]
    # Convert data into tuples
    data = [[tuple(map(int, tup.split(','))) for tup in line] for line in data]


    cave = form_cave(data)
    while True:
        rested = drop_sand(cave, (500,0))
        if rested == False:
            break
    print(sum(line.count('o') for line in cave))

def form_cave(data):
    # First find the dimensions for the cave
    # All coordinates are positive, just start from 0
    max_x = 0
    max_y = 0
    for line in data:
        x = max(line)[0]
        y = max(line, key=index_one)[1]
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    # added a floor 2 below y max, 
    # and an x max wide enough to make a pyramid up to the origin, plus a buffer
    max_x = max_x if max_x > (500 + max_y) else 500 + max_y
    cave = [['.' for i in range(max_y + 3)] for j in range(max_x + 5)]
    # Add the floor to the cave
    for i in range(len(cave)):
        cave[i][-1] = '#'
    # Determine if it's horizontal or vertical movement, and add to cave.
    for line in data:
        for i in range(1, len(line)):
            x_start, x_end = line[i-1][0], line[i][0]
            y_start, y_end = line[i-1][1], line[i][1]

            # Checking if y doesn't change
            if line[i-1][1] == line[i][1]:
                # Flipping values if end is less than start
                if x_end < x_start:
                    x_start, x_end = x_end, x_start
                for j in range(x_start, x_end + 1):
                    cave[j][y_start] = '#'
    
            else:
                if y_end < y_start:
                    y_start, y_end = y_end, y_start
                for j in range(y_start, y_end + 1):
                    cave[x_start][j] = '#'
    return cave

def drop_sand(cave, place):
    # Start at 500,0. Check for solid under, then under left, then under right.
    # If none available, then sand comes to rest as solid. Start over until it falls out of list.
    
    # Checking if origin is solid
    if cave[place[0]][place[1]] == 'o':
        return False
    if cave[place[0]][place[1]+1] == '.':
        x = drop_sand(cave, (place[0], place[1]+1))
        if x:
            return x
    elif cave[place[0]-1][place[1]+1] == '.':
        x = drop_sand(cave, (place[0]-1, place[1]+1))
        if x:
            return x
    elif cave[place[0]+1][place[1]+1] == '.':
        x = drop_sand(cave, (place[0]+1, place[1]+1))
        if x:
            return x
    else:
        cave[place[0]][place[1]] = 'o'
        return True


def index_one(_iter):
        return _iter[1]


if __name__ == '__main__':
    main()
