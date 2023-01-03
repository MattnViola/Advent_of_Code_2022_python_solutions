
# ore needs ore,clay needs ore,obsidian needs ore and clay,geode needs ore and obsidian
# tuple, list, dict? 

blueprints = []

with open('input.txt','r') as file:
    for line in file:
        l = line.strip('\n').split()
        x = [[l[6],0,0],[l[12],0,0],[l[18],l[21],0],[l[27],0,l[30]]]
        x = [[int(z) for z in y] for y in x]
        _dict = {'ore' : x[0], 'clay' : x[1], 'obsidian' : x[2], 'geode' : x[3]}
        blueprints.append(_dict)

# Need to find optimal way for obsidian generation by 24 minutes. branches are which robot to build. If not enough resources, wait the same amount of time until you can

blueprint_values = []
for blueprint in blueprints:
    most_geode = 0
    build_order_finder(blueprint,24,[1,0,0,0])

# Decide beforehand which to build, and then gather the resources for it.
def build_order_finder(blueprint,time,robots,resources=(0,0,0,0),design=None):
    global most_geode 
    if design:
        # Check if have resources, if not, wait, if goes over time, record most_geode and return. If have resources, then go through 1 time, and add robot
    for x in blueprint:
        build_order_finder(blueprint,time,robots,resources,design=x)
        
