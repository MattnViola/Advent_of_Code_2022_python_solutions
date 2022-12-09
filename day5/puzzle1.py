from stacks import stack
def main():
    with open('input.txt', 'r') as file:
        for line in file:
            move = line.strip().rsplit('\n')
            move = move[0].split()
            i = int(move[1])
            j = int(move[3]) - 1
            k = int(move[5]) - 1
            for _ in range(i):
                stack[k].append(stack[j][-1])
                stack[j] = stack[j][:-1]
        for i in range(len(stack)):
            print(stack[i][-1], end='')

if __name__ == "__main__":
    main()
    
        