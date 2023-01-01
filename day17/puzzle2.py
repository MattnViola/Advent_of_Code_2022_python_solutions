
def main():

    found = False
    remaining_blocks = 0
    stored_height = 0
    pattern_checker = {}

    with open('input.txt','r') as file:
        data = file.read()
    
    # Chamber indexing is y,x ; block indexing is x,y. Both are 0-indexed
    chamber = [['.'] * 7 for _ in range(1000000)]
    # Floor starts at 0
    chamber[0] = ['#'] * 7
    height = 0
    blocks_settled = 0
    # Coordinates of current block
    block = [(2,4), (3,4), (4,4), (5,4)]
    block_type = 1
    stop = False
    while True:
        jet_index = 0
        for jet in data:
            jet_index += 1            
            block = horizontal_move(jet, chamber, block)
            # If no collision below
            if vertical_check(chamber, block):
                block = list(map(lambda x: (x[0], x[1] - 1), block))
            else:
                # settle the block, update highest rock, get new block
                for x in block:
                    chamber[x[1]][x[0]] = '#'
                    if x[1] > height:
                        height = x[1]
                        
                
                block_type += 1
                x = block_type % 5
                match x:
                    case 0:
                        block = [(2,height + 4), (3,height + 4), (2,height + 5), (3,height + 5)]
                    case 1:
                        block = [(2,height + 4), (3,height + 4), (4,height + 4), (5,height + 4)]
                    case 2:
                        block = [(2,height + 5), (3,height + 4), (3,height + 5), (3,height + 6), (4,height + 5)]
                    case 3:
                        block = [(2,height + 4), (3,height + 4), (4,height + 4), (4,height + 5), (4,height + 6)]
                    case 4: 
                        block = [(2,height + 4), (2,height + 5), (2,height + 6), (2,height + 7)]
                blocks_settled += 1
                # Check for pattern
                if found == False:
                    if height > 30:
                            temp = (jet_index, block_type % 5, chamber[height - 30: height + 1])
                            for key in pattern_checker:
                                if temp == pattern_checker[key]:
                                    # If found, use the pattern to find out the height after 1000000000000 rocks settled.
                                    print(key, blocks_settled, height)
                                    # Find out pattern increment, add until the last pattern iteration before the big number. Continue until blocks_settled is the big number.
                                    stored_height = height
                                    pattern = (blocks_settled - key[0], height - key[1])
                                    pattern_repeats = (1000000000000 - blocks_settled) // pattern[0]
                                    height_added = pattern_repeats * pattern[1]
                                    blocks_settled += pattern_repeats * pattern[0]                             
                                    found = True
                                    break
                            if found == False:         
                                pattern_checker[(blocks_settled, height)] = temp
                else:
                    if blocks_settled == 1000000000000:
                        print(height + height_added)
                        stop = True
            if stop == True:
                break
        if stop == True:
                break
# Checks if block is obstructed. If not, moves the block left or right. Returns the block
def horizontal_move(jet, chamber, block):
    if jet == '>':
        for x in block:
            if x[0] == 6:
                return block
            if chamber[x[1]][x[0] + 1] == '#':
                return block
        return list(map(lambda x: (x[0] + 1, x[1]), block))
    else:
        for x in block:
            if x[0] == 0:
                return block
            if chamber[x[1]][x[0] - 1] == '#':
                return block
        return list(map(lambda x: (x[0] - 1, x[1]), block))

# Returns true if rock in the way    
def vertical_check(chamber, block):
    for x in block:
        if chamber[x[1] - 1][x[0]] == '#':
            return False
    return True


if __name__ == '__main__':
    main()


# What a mess!