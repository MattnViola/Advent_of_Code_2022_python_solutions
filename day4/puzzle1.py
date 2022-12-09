# Need to see if one range encompasses the other's range in a pair.

with open('puzzleinput.txt', 'r') as file:
    encompass = 0
    for line in file:
        pair = line.rstrip('\n').split(',')
        pair = [x.split('-') for x in pair]
        pair = [[int(y) for y in x] for x in pair]
            
        if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
            encompass += 1
            print(pair)
        elif pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]:
            encompass += 1
            print(pair)
    print(encompass)