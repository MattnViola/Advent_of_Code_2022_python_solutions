# Sides exposed to air bubbles dont count.


class Node:
    
    exposed = False
    exposed_amt = 0
    visited = []
    
    def __init__(self, coord, form):
        self.coord = coord
        self.form = form
        self.sides = []
        self.exposed = None
        
    def get_sides(self, cube):
        x,y,z = self.coord[0],self.coord[1],self.coord[2]
        sides = [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]
        for side in sides:
            try:
                if side[0] < 0 or side[1] < 0 or side[2] < 0:
                    self.sides.append(None)
                else:
                    self.sides.append(cube[side[0]][side[1]][side[2]])
            except IndexError:
                self.sides.append(None)
                
    # Checks if a side is exposed, if its the first time meeting an exposed node, increment amount and then make all nodes before it exposed == True                
    
    def check_exposed(self, start=True):
        if start:
            Node.exposed = False
            Node.visited.clear()
            if self.form == 'droplet':
                return
        if self.exposed == True:
            Node.exposed = True
            Node.exposed_amt += 1
            return
        if None in self.sides:
            self.exposed = True
            Node.exposed = True
            Node.exposed_amt += 1
            return               
        Node.visited.append(self)
        for side in self.sides:
            if side.form == 'air' and side not in Node.visited:
                if side.exposed == True:
                    self.exposed = True
                    Node.exposed = True
                    Node.exposed_amt += 1
                    return
                elif side.exposed == False:
                    continue
                else:
                    side.check_exposed(start=False)
                    if Node.exposed == True:
                        self.exposed = True
                        return
        self.exposed = False
        return

            
        
        

droplets = []

with open('input.txt','r') as file:
    # Finding largest integer
    cube_size = 0
    for line in file:
        line = list(map(int, line.strip('\n').split(',')))        
        for y in line:            
            if y > cube_size:
                    cube_size = y
        droplets.append(line)
        
# grace space
cube_size += 2
        
cube = [[[Node((x,y,z), 'air') for z in range(cube_size)] for y in range(cube_size)] for x in range(cube_size)]

# assign droplets to cube

for x,y,z in droplets:
    cube[x][y][z].form = 'droplet'
    
    
# Now collect sides 

for x in cube:
    for y in x:
        for node in y:
            node.get_sides(cube)
    
# Go through nodes, if form == droplet, check sides, if side is air, then try to find none
for x in cube:
    for y in x:
        for node in y:
            if node.form == 'air':
                continue
            for side in node.sides:
                if side == None:
                    Node.exposed_amt += 1
                    continue
                side.check_exposed()


print(Node.exposed_amt)

