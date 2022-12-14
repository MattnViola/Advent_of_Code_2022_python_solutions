# If both are ints, compare int. if not equal, first index should have lower. Shorter list should be first index.
# If both are lists, inspect elements in list, if not equal, first index should be lower, shorter nested list should be left.
# if one of each, convert integer to list, with that integer as its only value. then go to rules above.



# Sum of correct ordered pairs' indexes


def main():
    data = [None]
    correct_order = 0

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
        correct = compare(data[i][0], data[i][1])
        if correct == True:
            correct_order += i

    print(correct_order)

def compare(left, right):
    for i in range(min(len(left), len(right))):
        # Check if both are ints
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] != right[i]:
                correct = True if left[i] < right[i] else False
                return correct
        else:
            # If atleast one is list, convert any int to list
            if isinstance(left[i], int):
                left[i] = [left[i]]
            if isinstance(right[i], int):
                right[i] = [right[i]]
            # Compare those lists
            correct = compare(left[i], right[i])
            if correct == True or correct == False:
                return correct
     
    # If it gets through the list, check the length of the lists.
    if len(left) != len(right):
        correct = True if len(left) < len(right) else False
        return correct
    else:
        return

if __name__ == '__main__':
    main()   