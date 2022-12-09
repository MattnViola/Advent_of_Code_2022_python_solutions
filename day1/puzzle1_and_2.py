with open('list.txt', 'r') as calories:
    ind_cals = 0
    most = 0
    second_most = 0
    third_most = 0
    for line in calories:
        if line != '\n':
            i = int(line)
            ind_cals += i
        else:
            print(ind_cals)
            if ind_cals >= most:
                second_most = third_most
                most = second_most
                most = ind_cals
                ind_cals = 0
            elif ind_cals >= second_most:
                third_most = second_most
                second_most = ind_cals
                ind_cals = 0
            elif ind_cals >= third_most:
                third_most = ind_cals
                ind_cals = 0
            ind_cals = 0
                
    total = most + second_most + third_most
    print(total) 
    print(most)
    print(second_most)
    print(third_most)
        


#Need to sum up all the calories, detect a blank line, and then compare to greatest.

# Need to check for the top three elves. bottom to top!