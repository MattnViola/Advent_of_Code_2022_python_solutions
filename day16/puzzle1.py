
import collections

class Valve:
    
    # name : object
    valves = {}
    positive_valves = []
    queue = collections.deque()
    visited = []
    temp_pair_distance = {}

    def __init__(self, name, flow, connected):
        self.name = name
        self.flow = flow
        self.connected = connected
        Valve.valves[name] = self
        if self.flow > 0 or self.name == 'AA':
            Valve.positive_valves.append(self)
        self.pair_distance = None

    # Finds the shortest distance to each positive valve from current valve. Sets pair_distance as {object : distance}
    def pos_valve_distance(self, distance=0):
        if distance == 0:
            Valve.visited = []
            Valve.temp_pair_distance.clear()
            Valve.temp_pair_distance[self] = 0
            Valve.visited.append(self)
        for edge in self.connected:
            edge = Valve.valves[edge]
            if not edge in Valve.visited:
                Valve.queue.append((edge, distance + 1))
                Valve.visited.append(edge)
        if self.flow > 0:
            Valve.temp_pair_distance[self] = distance
        
        # Recursion until queue ends
        while Valve.queue:
            x = Valve.queue.popleft()
            x[0].pos_valve_distance(x[1])
        if distance == 0:
            self.pair_distance = Valve.temp_pair_distance.copy()
        return


best_path_value = 0
def main():
    global best_path_value

    with open('input.txt','r') as file:
        for line in file:
            line = line.rstrip('/n').split()
            # Parsing and putting the connected in a list
            connected = [valve.rstrip(',') for valve in line[9:]]
            Valve(line[1], int(line[4].rstrip(';').lstrip('rate=')), connected)


    for valve in Valve.positive_valves:
        valve.pos_valve_distance()

    simulate_paths(30, Valve.valves['AA'])
    print(best_path_value)
    

def simulate_paths(time, valve, released=0, rate=0, visited=[]):
    global best_path_value
    visited.append(valve.name)
    if time > 0:
        # If not starting valve, release
        if valve.name != 'AA':
            time -= 1
            released += rate
            rate += valve.flow
            if time == 0:
                best_path(released)
                visited.remove(valve.name)
                return

        for edge in valve.pair_distance:
            if not edge.name in visited:
                d = valve.pair_distance[edge]
                simulate_paths(time - d, edge, released + (rate*d), rate, visited)
        visited.remove(valve.name)
        released += abs(time) * rate
        best_path(released)
        return
    else:
        # If over time, subtract rate for the days over 0 from released, compare to best
        released -= abs(time) * rate
        best_path(released)
        visited.remove(valve.name)
        return

def best_path(x):
    global best_path_value
    if x > best_path_value:
        best_path_value = x
    return

if __name__ == '__main__':
    main()

