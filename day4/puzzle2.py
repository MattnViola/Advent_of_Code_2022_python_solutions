# Need to see if one range overlaps at all with the other pair.

with open('puzzleinput.txt', 'r') as file:
    encompass = 0
    for line in file:
        pair = line.rstrip('\n').split(',')
        pair = [x.split('-') for x in pair]
        pair = [[int(y) for y in x] for x in pair]
            
        if pair[1][0] <= pair[0][0] <= pair[1][1] or pair[1][0] <= pair[0][1] <= pair[1][1]:
            encompass += 1
            print(pair)
        elif pair[0][0] <= pair[1][0] <= pair[0][1] or pair[0][0] <= pair[1][1] <= pair[0][1]:
            encompass += 1
            print(pair)
    print(encompass)
    
    
# 2 ranges, say 2-5, 5-7
# if a lower bound is lower than the other bound, and the higher is lower, then they dont overlap.
# if a lower bound is higher than both the other's lower and higher bound, then they dont overlap.

# if a lower bound is greater than or equal to lower bound, and less than or equal to a higher bound then they overlap.
# if a higher bound is greater than or equal to lower bound, and less than or equal to a higher bound then they overlap.

# 1-4, 3-5