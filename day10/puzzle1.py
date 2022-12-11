# if addx instruction is read, 2 cycles happen before the next instruction is read.


with open("input.txt", "r") as file:
    data = [line.rstrip("\n").split() for line in file]

data = [[x[0], int(x[1])] if len(x) == 2 else [x[0]] for x in data]

req_cycle = [20, 60, 100, 140, 180, 220]
strengths = []
x = 1
cycle = 0
for instruction in data:
    for i in range(len(instruction)):
        cycle += 1
        if cycle in req_cycle:
            strengths.append(cycle * x)
    if len(instruction) == 2:
        x += instruction[1]


print(sum(strengths))
