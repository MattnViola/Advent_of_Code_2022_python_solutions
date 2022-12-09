# groups of 3 elves have a unique char that they all have. That is the only char that the group of 3 similarily have.
# Need to identify for each three lines the common character, ord them, and then sum them up.

with open('puzzleinput.txt', 'r') as input:
    line_number = -1
    group = ['','','']
    sum = 0
    matches = 0
    for line in input:
        # index 0
        line_number +=1
        ruck = line.rstrip('\n')
        group[(line_number % 3)] = ruck
        if line_number % 3 == 2:   
            for i in range(len(ruck)):
                if ruck[i] in group[0] and ruck[i] in group[1]:
                    if ruck[i].isupper():
                        sum += ord(ruck[i]) - 38
                        matches += 1
                    elif ruck[i].islower():
                        sum += ord(ruck[i]) - 96
                        matches += 1
                    break
    print(sum)
    print(matches)