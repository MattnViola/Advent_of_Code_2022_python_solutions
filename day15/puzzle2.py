# Now need to find the only place a beacon could exists between x,y 0 and 4 mil

def main():

    sensors = []
    # Beacon x,y
    beacons = set()


    with open('input.txt','r') as file:
        for line in file:
            line = line.rstrip('\n').split()
            s_x, s_y = int(line[2].lstrip('x=').rstrip(',')), int(line[3].lstrip('y=').rstrip(':'))
            b_x, b_y = int(line[8].lstrip('x=').rstrip(',')), int(line[9].lstrip('y='))

            # Add beacon coord
            beacons.add((b_x, b_y))

            # Find distance from beacon and add to y2m
            x_diff, y_diff = abs(b_x - s_x), abs(b_y - s_y)
            total_diff = x_diff + y_diff
            sensors.append((s_x, s_y, total_diff))

    edges_check(sensors, beacons)



#check the edges + 1 of each sensor area
def edges_check(sensors, beacons):
    for s_x,s_y,diff in sensors:
        for x_edge in range(diff + 2):
            y_edge = (diff + 1) - x_edge
            added = [(s_x + x_edge, s_y + y_edge), (s_x + x_edge, s_y - y_edge), (s_x - x_edge, s_y - y_edge), (s_x - x_edge, s_y - y_edge)]
            for coord in added:
                if not (0 <= coord[0] <= 4000000) or not (0 <= coord[1] <= 4000000):
                    continue
                if coord in beacons:
                    continue
                if coord_check(coord, sensors):
                    print(coord[0]*4000000 + coord[1])
                    return
            
# After getting an edge piece, check if its in the area of another sensor
def coord_check(coord, sensors):
    # Check if the distance between the coord and all sensors. if it is less than the distance to a sensor's closest beacon, return False
    for s_x, s_y, diff in sensors:
        coord_distance = abs(coord[0] - s_x) + abs(coord[1] - s_y)
        if coord_distance <= diff:
            return False

    return True
        
                
if __name__ == '__main__':
    main()