import math

# Only first 3 blueprints, 32 mins


# ore needs ore,clay needs ore,obsidian needs ore and clay,geode needs ore and obsidian
most_geode = 0
def main():
    global most_geode

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
    for i in range(3):
        most_geode = 0
        build_order_finder(blueprints[i],32,(1,0,0,0))
        blueprint_values.append(most_geode)
    print(math.prod(blueprint_values))

    # Decide beforehand which to build, and then gather the resources for it.
def build_order_finder(blueprint,time,robots,resources=(0,0,0,0),design=None):
    global most_geode
    if design:
        # Check to see if there's any chance this branch can be higher than most_geode.
        # Can only make 1 geode robot at a time.
        n = time - 1
        most_possible = (n*(n+1))/2 + (robots[3] * time) + resources[3]
        if most_possible <= most_geode:
            return
        req_resources = blueprint[design]
        for i in reversed(range(3)):
            # Check if have resources, if not, continue time forward until you do
            if resources[i] < req_resources[i]:
                # If no robots for required resource, return
                if robots[i] == 0:
                    return
                time_needed = (req_resources[i] - resources[i]) // robots[i]
                if (req_resources[i] - resources[i]) % robots[i] != 0:
                    time_needed += 1
                time -= time_needed
                resources = resource_gain(time_needed,resources,robots)
                # If over time.
                if time <= 0:
                    geodes_check(resources[3] + time * robots[3])
                    return
        # Have resources, so go forward 1 day and generate the robot
        time -= 1
        resources = resource_gain(1,resources,robots)
        if time <= 0:
            geodes_check(resources[3] + time * robots[3])
            return
        robots = list(robots)
        robots[list(blueprint.keys()).index(design)] += 1
        robots = tuple(robots) 
        # Subtract used resources
        temp = list(map(lambda x,y: x - y, resources, req_resources))
        temp.append(resources[3])
        resources = tuple(temp)


    for x in reversed(blueprint):
        build_order_finder(blueprint,time,robots,resources,design=x)
    return
        

def geodes_check(geodes):
    global most_geode
    if geodes > most_geode:
        most_geode = geodes

def resource_gain(time_passed, resources, robots):
    x = []
    for j in range(4):
        x.append(resources[j] + robots[j] * time_passed) 
    return tuple(x)

main()
