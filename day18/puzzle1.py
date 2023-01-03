

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
        
cube = [[[None]*cube_size for _ in range(cube_size)] for _ in range(cube_size)]

# assign droplets to cube

for x,y,z in droplets:
    cube[x][y][z] = '#'
    
# Check exposed sides
exposed = 0
for x in range(len(cube)):
    for y in range(len(cube[x])):
        for z in range(len(cube[x][y])):
            if cube[x][y][z] == '#':
                sides = [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]
                for side in sides:
                    if cube[side[0]][side[1]][side[2]] == None:
                        exposed += 1

print(exposed)
                
                
    
