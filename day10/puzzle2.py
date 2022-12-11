#


with open("input.txt", "r") as file:
    data = [line.rstrip("\n").split() for line in file]

data = [[x[0], int(x[1])] if len(x) == 2 else [x[0]] for x in data]

crt = [["."] * 40 for i in range(6)]

x = 1
crt_line = 0
cycle = 0
for instruction in data:
    for _ in range(len(instruction)):
        # Checking if sprite is lit up
        if -1 <= (cycle - x) <= 1:
            crt[crt_line][cycle] = "#"
        cycle += 1
        # Checking if CRT is going to a new line
        if cycle == 40:
            cycle = 0
            crt_line += 1
        print(x)
    if len(instruction) == 2:
        x += instruction[1]

for line in crt:
    print(*line)
