from collections import deque

class Node:
    
    def __init__(self, number):
        self.number = number

order = []

with open('input.txt','r') as file:
    for line in file:
        order.append(Node(int(line.rstrip('\n'))))
        

# Decrypt
y = deque(order.copy())
L = len(y)
for x in order:
    movement = x.number
    place = y.index(x)
    if place + movement >= L or place + movement <= 0:
        new_place = (movement + place) % (L - 1)
    else:
        new_place = movement + place
    y.remove(x)
    y.insert(new_place, x)

# Find 1000, 2000, 3000th number after the value 0
for x in range(L):
    if y[x].number == 0:
        z = x
    
y.rotate(-z)
# Assuming deque is longer than 3000
x = [y[1000].number,y[2000].number,y[3000].number]
print(sum(x))


