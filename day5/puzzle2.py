from stacks import stack
def main():
    with open('input.txt', 'r') as file:
        for line in file:
            move = line.strip().rsplit('\n')
            move = move[0].split()
            i = int(move[1])
            j = int(move[3]) - 1
            k = int(move[5]) - 1
            for l in reversed(range(1,i + 1)):
                stack[k].append(stack[j][-l])
            stack[j] = stack[j][:-i]
        for i in range(len(stack)):
            print(stack[i][-1], end='')

if __name__ == "__main__":
    main()
    
# Need to change from moving one crate at a time to moving multiple
#Need to iterate over stack[n][i] when appending. and then remove more