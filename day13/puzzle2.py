# Need to organize them all now, with [[2]] and [[6]] added
# Then multiply the indexes of the two above.

def main():
    data = [None]
    correct_order = 0

    with open('input.txt','r') as file:
        for line in file:
            if line != '\n':
                data.append(eval(line.rstrip('\n')))
    # Append the 2 extra
    data.append([[2]])
    data.append([[6]])
    # Bubble Sort
    while True:
        sorts = 0
        for i in range(2, len(data)):
            correct = compare(data[i-1],data[i])
            if not correct:
                data[i-1], data[i] = data[i], data[i-1]
                sorts += 1
        if sorts == 0:
            break
    x = data.index([[2]])
    y = data.index([[6]])
    print(x*y)


def compare(left, right):
    # Make a shallow copy so that the lists won't be changed
    left,right = left[:],right[:]
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