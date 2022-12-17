# If both are ints, compare int. if not equal, first index should have lower. Shorter list should be first index.
# If both are lists, inspect elements in list, if not equal, first index should be lower, shorter nested list should be left.
# if one of each, convert integer to list, with that integer as its only value. then go to rules above.


data = [None]
correct_order = []

with open('input.txt','r') as file:
    pair = []
    for line in file:
        line = line.rstrip('\n')
        if line == '':
            data.append(pair)
            pair = []
        else:
            pair.append(eval(line))
            
for i in range(1, len(data)):
    # Checking the longest list size and iterating over it.
    for j in range(max(len(data[i][0]), len(data[i][1]))):
        # Checking if one list is out of indexes
        try:
            left = data[i][0][j]
        except:
            correct_order.append(i)
            break
        try:
            right = data[i][1][j]
        except:
            break
        
        if type(data[i][0]) == type(data[i][1]):
        
def compare(left, right):

    
# Need to loop through nested lists, checking if at least one of them has an integer, and then evaluating that.
    