

# Sensor coords and distance to beacon (0,0,0)
sen_beac = []
# Beacons at 2mil y coord
y2mbeacon = set()
# Set of where a beacon cannot be
y2m = set()
with open('input.txt','r') as file:
    for line in file:
        line = line.rstrip('\n').split()
        s_x, s_y = int(line[2].lstrip('x=').rstrip(',')), int(line[3].lstrip('y=').rstrip(':'))
        b_x, b_y = int(line[8].lstrip('x=').rstrip(',')), int(line[9].lstrip('y='))
        # Check to see if a beacon is at y=2mil, because then that is not 'cannot be a beacon'
        if b_y == 2000000:
            y2mbeacon.add(b_x)
        x_diff, y_diff = abs(b_x - s_x), abs(b_y - s_y)
        total = x_diff + y_diff
        sen_beac.append((s_x, s_y, total))
# take from difference to get to y=2mil. Add that to set. Then with the rest of the distance, go left and right and add to the set.
for sens in sen_beac:
    remainder = sens[2] - abs(sens[1] - 2000000)
    # Checking if got to 2mil y coord
    if remainder < 0:
        continue
    if remainder >= 0:
        for i in range(0, remainder + 1):
            y2m.add(sens[0] + i)
            y2m.add(sens[0] - i)
# Remove beacons from y2m
for coord in y2mbeacon:
    y2m.discard(coord)

print(len(y2m))
