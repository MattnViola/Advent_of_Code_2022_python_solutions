
f_units = []
longest_num = 0
with open('input.txt','r') as file:
    for line in file:
        f_units.append(list(line.strip('\n')))
        if len(line) > longest_num:
            longest_num = len(line)
# Convert to integers
_dict = {'-' : '-1', '=' : '-2', -1 : '-', -2 : '='}

# Reversed so that it starts with the lowest integer
f_units = [list(reversed([int(_dict[u]) if u in _dict else int(u) for u in f])) for f in f_units]


# Add the places of each value together
sums = [0]
for i in range(longest_num):
    if i == len(sums):
        sums.append(0)
    for u in f_units:
        if i >= len(u):
            continue
        sums[i] += u[i]
print(sums)
# Convert 5-decimal and if above 2, add one and subtract 5 again.
for i in range(len(sums)):
    d = sums[i] // 5
    r = sums[i] % 5
    if r > 2:
        d += 1
        r -= 5
    if i+1 == len(sums):
        sums.append(0)
    sums[i+1] += d
    sums[i] = r
print(sums)
answer = [_dict[u] if u in _dict else str(u) for u in sums]
print(*reversed(answer))
        

