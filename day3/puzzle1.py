# Need to determine line length and split each line in half THEY ARE ALL EVEN.
# Then, need to determine common letters in each line, case-sensitive. 
# Then, need to convert those to integers and add them up.

with open('puzzleinput.txt', 'r') as input:
    sum = 0
    matches = 0
    for line in input:
        ruck = line.rstrip('\n')
        half = len(ruck) // 2
        comp1 = ruck[:half]
        comp2 = ruck[half:]
        for i in range(len(comp1)):
            if comp1[i] in comp2:
                print(comp1[i] + ' : ' + comp2)
                if comp1[i].isupper():
                    sum += ord(comp1[i]) - 38
                    matches += 1
                elif comp1[i].islower():
                    sum += ord(comp1[i]) - 96
                    matches += 1
                break
    print(sum)
    print(matches)


    
        

